# Run satisfiability checking with Z3.

import argparse as ap
import sys
import os
import re
import math
import multiprocessing
import time
from z3 import *
from utils.Shell import Shell
from utilities import get_abc_result_line

parser = ap.ArgumentParser(description = 'Run Quacky on AWS IAM policies')
parser.add_argument('-d', '--dir', help = 'Policy Directory', required = True)
parser.add_argument('-v', '--verbose', help = 'Verbose', required = False, action = 'store_true')
parser.add_argument('-c', '--constraints', help = 'use resource type constraints', required = False, action = 'store_true')
parser.add_argument('-e', '--enc', help = 'use action encoding', required = False, action = 'store_true')
parser.add_argument('-t', '--timeout', help = 'Timeout', required = False, default = 120)
args = parser.parse_args()

single_policy_dir = os.fsencode('../samples/' + args.dir + '/exp_single/')

def get_sat(F):
    s = Solver()
    s.add(F)
    return s.check() == sat

def call_z3(path, policy):
    shell = Shell()

    #Translate policies into SMT constraint formula
    cmd = 'python3 translator.py -p1 {}/{} -s'.format(path, policy)
    if args.constraints:
        cmd += ' -c'
    if args.enc:
        cmd += ' -e'

    out, err = shell.runcmd(cmd)
    if args.verbose:
        print(out, err)

    #Call Z3 on the outputted policy translation
    ifile = open('output_1.smt2', 'r')
    formula = ifile.read()
    ifile.close()

    z3_time = time.time()
    f = parse_smt2_file('output_1.smt2')
    is_sat = get_sat(f)
    z3_time = (time.time() - z3_time) * 1000
    
    #Populate the markdown table with the results
    if is_sat:
        md = '|[{}/{}]({}/{})|{}|{}|'.format(path, policy, path, policy, 'SAT', z3_time)
    else:
        md = '|[{}/{}]({}/{})|{}|{}|'.format(path, policy, path, policy, 'UNSAT', z3_time)

    print(md)
    return

#Print out test description
print()
print('**Policies in {}**'.format(args.dir))
print()

#Set up markdown table
print('|Policy|SAT/UNSAT|Solve Time (ms)|')
print('|-|-|-|')

#Iterate through all policies within directory and perform check.
for dir in os.listdir(single_policy_dir):
    path = os.fsdecode(single_policy_dir) + os.fsdecode(dir)
    for file in os.listdir(path):
        policy = os.fsdecode(file)
        if policy.endswith('.json'):
            t = multiprocessing.Process(target = call_z3, args=(path, policy))
            t.start()
            t.join(timeout = float(args.timeout))
            if t.is_alive():
                t.terminate()
                md = '|[{}/{}]({}/{})|{}|{}|'.format(path, policy, path, policy, 'TIMEOUT', args.timeout)
                print(md)
