# Run Quacky on single AWS IAM policies. Analyze permissiveness.

import argparse as ap
import sys
import os
import re
import math
from utils.Shell import Shell
from utilities import get_abc_result_line

parser = ap.ArgumentParser(description = 'Run Quacky on AWS IAM policies')
parser.add_argument('-d', '--dir', help = 'Policy Directory', required = True)
parser.add_argument('-v', '--verbose', help = 'Verbose', required = False, action = 'store_true')
parser.add_argument('-c', '--constraints', help = 'use resource type constraints', required = False, action = 'store_true')
parser.add_argument('-e', '--enc', help = 'use action encoding', required = False, action = 'store_true')
parser.add_argument('-s', '--smt-lib', help = 'use SMT-LIB syntax', required = False, action = 'store_true')
parser.add_argument('-b', '--bound', help = 'Bound', required = True)
parser.add_argument('-f', '--variable', help = 'count all variables', required = False, action = 'store_true')
args = parser.parse_args()

single_policy_dir = os.fsencode('../samples/' + args.dir + '/exp_single/')

def call_abc(path, policy):
    shell = Shell()

    #Translate policies into SMT constraint formula
    cmd = 'python3 translator.py -p1 {}/{}'.format(path, policy)
    if args.constraints:
        cmd += ' -c'
    if args.enc:
        cmd += ' -e'
    if args.smt_lib:
        cmd += ' -s'

    out, err = shell.runcmd(cmd)
    if args.verbose:
        print(out, err)

    #Call ABC on the outputted policy translation
    cmd = 'abc -bs {} -v 0 -i output_1.smt2 --count-tuple'.format(args.bound)
    if args.variable:
        cmd += ' --count-variable principal,action,resource'
    
    out, err = shell.runcmd(cmd)
    if args.verbose:
        print(out, err)

    #Parse output of ABC to get a dictionary of the results
    result = get_abc_result_line(out,err)

    #Populate the markdown table with the results
    if result['is_sat'] == "SAT":
        md = '|[{}/{}]({}/{})|{}|{}|{}|{}|'.format(path, policy, path, policy, 
            result['is_sat'], result['solve_time'],
            math.log(int(result['count']), 2), result['count_time']
        )

        if args.variable:
            md += '{}|{}|{}|'.format(
                math.log(int(result['var']['principal']['count']),2), 
                math.log(int(result['var']['action']['count']),2), 
                math.log(int(result['var']['resource']['count']),2)
            )
        
    else:
        md = '|[{}/{}]({}/{})|{}|{}|-|-|'.format(path, policy, path, policy, 
            result['is_sat'], 
            result['solve_time']
        )

        if args.variable: 
            md += '-|-|-|'

    print(md)

    #Make directories within the same directory as the policy and store the translation in this new directory.
    out, err = shell.rmrdir('{}/abc_{}'.format(path, policy.replace('.json', '')))
    if args.verbose:
        print(out, err)

    out, err = shell.mkdir('{}/abc_{}'.format(path, policy.replace('.json', '')))
    if args.verbose:
        print(out, err)

    out, err = shell.mv('output_1.smt2', '{}/abc_{}'.format(path, policy.replace('.json', '')))
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
    print('|Policy|SAT/UNSAT|Solve Time (ms)|lg(tuple)|Count Time (ms)|lg(principal)|lg(action)|lg(resource)|')
    print('|-|-|-|-|-|-|-|-|')
else:
    print('|Policy|SAT/UNSAT|Solve Time (ms)|lg(tuple)|Count Time (ms)|')
    print('|-|-|-|-|')

#Iterate through all policies within directory and perform check.
for dir in os.listdir(single_policy_dir):
    path = os.fsdecode(single_policy_dir) + os.fsdecode(dir)
    for file in os.listdir(path):
        policy = os.fsdecode(file)
        if policy.endswith('.json'):
            try:
                call_abc(path, policy)
            except:
                pass
