# Run Quacky on multiple AWS IAM policies.
# Analyze relative permissiveness.

import argparse as ap
import sys
import os
import re
import math
from utils.Shell import Shell
from utilities import get_abc_result_line

parser = ap.ArgumentParser(description = 'Translate IAM policies to SMT-LIB2 for ABC/Z3')
parser.add_argument('-d', '--dir', help = 'Policy Directory', required = True)
parser.add_argument('-v', '--verbose', help = 'Verbose', required = False, action = 'store_true')
parser.add_argument('-c', '--constraints', help = 'use resource type constraints', required = False, action = 'store_true')
parser.add_argument('-e', '--enc', help = 'use action encoding', required = False, action = 'store_true')
parser.add_argument('-s', '--smt-lib', help = 'use SMT-LIB syntax', required = False, action = 'store_true')
parser.add_argument('-b', '--bound', help = 'Bound', required = True)
parser.add_argument('-f', '--variable', help = 'count all variables', required = False, action = 'store_true')
args = parser.parse_args()

multiple_policy_dir = os.fsencode('../samples/' + args.dir + '/exp_multiple/')

def call_abc(path, p1, p2):
    shell = Shell()

    #Translate policies into SMT constraint formula
    cmd = 'python3 translator.py -p1 {}/{} -p2 {}/{}'.format(path, p1, path, p2)
    if args.constraints:
        cmd += ' -c'
    if args.enc:
        cmd += ' -e'
    if args.smt_lib:
        cmd += ' -s'
    
    out, err = shell.runcmd(cmd)
    if args.verbose:
        print(out, err)
 
    #Call ABC on the domain translation
    cmd = 'abc -bs {} -v 0 -i output_0.smt2 --precise --count-tuple'.format(args.bound)
    if args.variable:
        cmd += ' --count-variable principal,action,resource'
    
    out, err = shell.runcmd(cmd)
    if args.verbose:
        print(out,err)
    
    #Parse output of ABC to get a dictionary of the results
    result0 = get_abc_result_line(out,err)
   
    #Call ABC on the first outputted translation
    cmd = 'abc -bs {} -v 0 -i output_1.smt2 --precise --count-tuple'.format(args.bound)
    if args.variable:
        cmd += ' --count-variable principal,action,resource'
    
    out, err = shell.runcmd(cmd)
    if args.verbose:
        print(out, err)
    
    #Parse output of ABC to get a dictionary of the results
    result1 = get_abc_result_line(out,err)
    
    #Call ABC on the second outputted translation
    cmd = 'abc -bs {} -v 0 -i output_2.smt2 --precise --count-tuple'.format(args.bound)
    if args.variable:
        cmd += ' --count-variable principal,action,resource'
    
    out, err = shell.runcmd(cmd)
    if args.verbose:
        print(out,err)
    
    #Parse output of ABC to get a dictionary of the results
    result2 = get_abc_result_line(out,err)

    #Populate the markdown table with the results
    md = ''
    md += '|[{}/{}]({}/{})|[{}/{}]({}/{})|'.format(path, p1, path, p1, path, p2, path, p2)
    if result1['is_sat'] == 'sat':
        md += '{}|{}|{}|{}|'.format(result1['is_sat'], result1['solve_time'], 
            math.log(int(result1['count']),2), result1['count_time']
        )
        if args.variable:
            md += '{}|{}|{}|'.format(
                math.log(int(result1['var']['principal']['count']),2), 
                math.log(int(result1['var']['action']['count']),2), 
                math.log(int(result1['var']['resource']['count']),2)
            )
        if args.ppd:
            if result0['is_sat'] == 'SAT':
                md += '{}|'.format(math.log(int(result1['count']),2) / math.log(int(result0['count'])),2)
            else:
                md += '-|'

    else:
        md += '{}|{}|-|-|'.format(result1['is_sat'], result1['solve_time'])
        if args.variable: 
            md += '-|-|-|'
        if args.ppd: 
            md += '-|'

    if result2['is_sat'] == 'sat':
        md += '{}|{}|{}|{}|'.format(result2['is_sat'], result2['solve_time'], 
            math.log(int(result2['count']),2), result2['count_time']
        )
        if args.variable:
            md += '{}|{}|{}|'.format(
                math.log(int(result2['var']['principal']['count']),2),
                math.log(int(result2['var']['action']['count']),2),
                math.log(int(result2['var']['resource']['count']),2)
            )
        if args.ppd:
            if result0['is_sat'] == 'SAT':
                md += '{}|'.format(math.log(int(result2['count']),2) / math.log(int(result0['count']),2))
            else:
                md += '-|'

    else:
        md += '{}|{}|-|-|'.format(result2['is_sat'], result2['solve_time'])  
        if args.variable: 
            md += '-|-|-|'
        if args.ppd:
            md += '-|'
    if args.ppd:
        if result0['is_sat'] == 'SAT':
            md += '{}|'.format(math.log(int(result0['count']),2))
        else:
            md += '-|'
    print(md)

    #Make directories within the same directory as the policy and store the translation in this new directory.
    out, err = shell.rmrdir('{}/abc_{}_{}'.format(path, p1.replace('.json', ''), p2.replace('.json', '')))
    if args.verbose:
        print(out, err)

    out, err = shell.mkdir('{}/abc_{}_{}'.format(path, p1.replace('.json', ''), p2.replace('.json', '')))
    if args.verbose:
        print(out, err)

    out, err = shell.mv('output_0.smt2', '{}/abc_{}_{}'.format(path, p1.replace('.json', ''), p2.replace('.json', '')))
    if args.verbose:
        print(out, err)

    out, err = shell.mv('output_1.smt2', '{}/abc_{}_{}'.format(path, p1.replace('.json', ''), p2.replace('.json', '')))
    if args.verbose:
        print(out, err)
    
    out, err = shell.mv('output_2.smt2', '{}/abc_{}_{}'.format(path, p1.replace('.json', ''), p2.replace('.json', '')))
    if args.verbose:
        print(out, err)

#Print out test description
print()
print('**Policies in {}**'.format(args.dir))
print()
print('bound: `{}`, variables: `{}`, constraints: `{}`, encoding: `{}`, smt-lib: `{}`'.format(args.bound, args.variable, args.constraints, args.enc, args.smt_lib))
print()

#Set up markdown table
if args.variable:
    print('|Policy 1|Policy 2|P1 => P2|Solve Time (ms)|lg(tuple)|Count Time (ms)|lg(principal)|lg(action)|lg(resource)|P2 => P1|Solve Time (ms)|lg(tuple)|Count Time (ms)|lg(principal)|lg(action)|lg(resource)|')
    print('|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|')
elif args.ppd:
    print('|Policy 1|Policy 2|P1 => P2|Solve Time (ms)|lg(tuple)|Count Time (ms)|% Domain|P2 => P1|Solve Time (ms)|lg(tuple)|Count Time (ms)|% Domain|lg(domain)|')
    print('|-|-|-|-|-|-|-|-|-|-|-|-|-|')
else:
    print('|Policy 1|Policy 2|P1 => P2|Solve Time (ms)|lg(tuple)|Count Time (ms)|P2 => P1|Solve Time (ms)|lg(tuple)|Count Time (ms)|')
    print('|-|-|-|-|-|-|-|-|-|-|')

#Iterate through all policies within directory and perform check.
for dir in os.listdir(multiple_policy_dir):
    path = os.fsdecode(multiple_policy_dir) + os.fsdecode(dir)
    n = len(os.listdir(path))
    for i in range(n):
        for j in range(i + 1,n):
            p1 = os.fsdecode(os.listdir(path)[i])
            p2 = os.fsdecode(os.listdir(path)[j])
            if p1.endswith('.json') and p2.endswith('.json'):
                call_abc(path, p1, p2)
