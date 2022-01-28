# Run Quacky on original vs mutant AWS IAM policies.
# Analyze relative permissiveness.

import argparse as ap
import sys
import os
import re
import math
import multiprocessing
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
parser.add_argument('-t', '--timeout', help = 'Timeout', required = False, default = 120)
args = parser.parse_args()

orig_policy_dir = os.fsencode('../samples/' + args.dir + '/exp_single/')
mutated_policy_dir = os.fsencode('../samples/mutations/' + args.dir + '/exp_single/')

def call_abc(orig_path, mutated_path, p1, p2):
    shell = Shell()
    
    #Translate policies into SMT constraint formula
    cmd = 'python3 translator.py -p1 {}/{} -p2 {}/{}'.format(orig_path, p1, mutated_path, p2)
    if args.constraints:
        cmd += ' -c'
    if args.enc:
        cmd += ' -e'
    if args.smt_lib:
        cmd += ' -s'

    out, err = shell.runcmd(cmd)
    if args.verbose:
        print(out, err)
   
    #Call ABC on the first outputted translation
    cmd = 'timeout {}s '.format(args.timeout)
    cmd += 'abc -bs {} -v 0 -i output_1.smt2 --precise --count-tuple --cache-subformula --cache-automata'.format(args.bound)
    if args.variable:
        cmd += ' --count-variable principal,action,resource'
    
    out, err = shell.runcmd(cmd)
    if args.verbose:
        print(out, err)
    
    #Parse output of ABC to get a dictionary of the results
    result1 = get_abc_result_line(out,err)
    
    #Call ABC on the second outputted translation
    cmd = 'timeout {}s '.format(args.timeout)
    cmd = 'abc -bs {} -v 0 -i output_2.smt2 --precise --count-tuple --cache-subformula --cache-automata'.format(args.bound)
    if args.variable:
        cmd += ' --count-variable principal,action,resource'
    
    out, err = shell.runcmd(cmd)
    if args.verbose:
        print(out,err)
    
    #Parse output of ABC to get a dictionary of the results
    result2 = get_abc_result_line(out,err)

    #Populate the markdown table with the results
    md = ''
    md += '|[{}/{}]({}/{})|[{}/{}]({}/{})|'.format(orig_path, p1, orig_path, p1, mutated_path, p2, mutated_path, p2)
    if result1['is_sat'] == "SAT" and 'count' in result1.keys():
        md += '{}|{}|{}|{}|'.format(result1['is_sat'], result1['solve_time'], 
            result1['count'], result1['count_time']
        )
        if args.variable:
            md += '{}|{}|{}|'.format(
                result1['var']['principal']['count'], 
                result1['var']['action']['count'], 
                result1['var']['resource']['count']
            )

    else:
        md += '{}|{}|-|-|'.format(result1['is_sat'], result1['solve_time'])
        if args.variable: 
            md += '-|-|-|'

    if result2['is_sat'] == "SAT" and 'count' in result2.keys():
        md += '{}|{}|{}|{}|'.format(result2['is_sat'], result2['solve_time'], 
            result2['count'], result2['count_time']
        )
        if args.variable:
            md += '{}|{}|{}|'.format(
                result2['var']['principal']['count'],
                result2['var']['action']['count'],
                result2['var']['resource']['count']
            )

    else:
        md += '{}|{}|-|-|'.format(result2['is_sat'], result2['solve_time'])  
        if args.variable: 
            md += '-|-|-|'

    print(md)

    #Make directories within the same directory as the policy and store the translation in this new directory.
    out, err = shell.rmrdir('{}/abc_{}_{}'.format(mutated_path, p1.replace('.json', ''), p2.replace('.json', '')))
    if args.verbose:
        print(out, err)

    out, err = shell.mkdir('{}/abc_{}_{}'.format(mutated_path, p1.replace('.json', ''), p2.replace('.json', '')))
    if args.verbose:
        print(out, err)

    out, err = shell.mv('output_0.smt2', '{}/abc_{}_{}'.format(mutated_path, p1.replace('.json', ''), p2.replace('.json', '')))
    if args.verbose:
        print(out, err)

    out, err = shell.mv('output_1.smt2', '{}/abc_{}_{}'.format(mutated_path, p1.replace('.json', ''), p2.replace('.json', '')))
    if args.verbose:
        print(out, err)
    
    out, err = shell.mv('output_2.smt2', '{}/abc_{}_{}'.format(mutated_path, p1.replace('.json', ''), p2.replace('.json', '')))
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
else:
    print('|Policy 1|Policy 2|P1 => P2|Solve Time (ms)|lg(tuple)|Count Time (ms)|P2 => P1|Solve Time (ms)|lg(tuple)|Count Time (ms)|')
    print('|-|-|-|-|-|-|-|-|-|-|')

timed_out = []

#Iterate through all policies within directory and perform check.
for dir in os.listdir(orig_policy_dir):
    orig_path = os.fsdecode(orig_policy_dir) + os.fsdecode(dir)
    for orig_policy in os.listdir(orig_path):
        if orig_policy.endswith('.json'):
            mutated_path = mutated_policy_dir + dir + b'/' + os.fsencode(orig_policy.replace('.json', ''))
            mutated_path = os.fsdecode(mutated_path)  
            try:
                os.listdir(mutated_path)
            except:
                continue
            for mutated_policy in os.listdir(mutated_path):
                if mutated_policy.endswith('.json'):
                    t = multiprocessing.Process(target = call_abc, args=(orig_path, mutated_path, orig_policy, mutated_policy))
                    t.start()
                    t.join(timeout = float(args.timeout))
                    if t.is_alive():
                        t.terminate()
                        timed_out.append(mutated_path + '/' + mutated_policy)

print()
print('**Timed out**')
for policy in timed_out:
    print(policy)
