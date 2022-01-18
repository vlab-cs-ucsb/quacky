# Run enumerative model counting with Z3 vs ABC.

import argparse as ap
import sys
import os
import re
import math
import multiprocessing
import time
from utils.Shell import Shell
from utilities import get_abc_result_line
from allSat import get_models
from z3 import *

parser = ap.ArgumentParser(description = 'Run Quacky on AWS IAM policies')
parser.add_argument('-d', '--dir', help = 'Policy Directory', required = True)
parser.add_argument('-v', '--verbose', help = 'Verbose', required = False, action = 'store_true')
parser.add_argument('-c', '--constraints', help = 'use resource type constraints', required = False, action = 'store_true')
parser.add_argument('-e', '--enc', help = 'use action encoding', required = False, action = 'store_true')
parser.add_argument('-b', '--bound', help = 'Bound', required = True)
parser.add_argument('-t', '--timeout', help ='Timeout (sec)', required = True) 
args = parser.parse_args()

single_policy_dir = os.fsencode('../samples/' + args.dir + '/exp_single/')

def call_solvers(path, policy):
    shell = Shell()
    # Translate policies into SMT constraint formula
    cmd = 'python3 translator.py -p1 {}/{} -s'.format(path, policy)
    if args.constraints:
        cmd += ' -c'
    if args.enc:
        cmd += ' -e'

    out, err = shell.runcmd(cmd)
    if args.verbose:
        print(out, err)
    
    ifile = open('output_1.smt2', 'r')
    formula = ifile.read()
    ifile.close()
    LOOKUP = '(check-sat)'
    formula = formula.replace(LOOKUP, '(assert (<= (str.len resource) {}))\n'.format(args.bound) + LOOKUP)
    ofile = open('output_1.smt2', 'w')
    ofile.write(formula)
    ofile.close()

    z3_time = time.time()
    f = parse_smt2_file('output_1.smt2')
    result, models = get_models(f, int(args.timeout))
    z3_time = (time.time() - z3_time) * 1000
    z3_count = models

    # Call ABC for policy
    cmd = 'abc -bs {} -v 0 -i output_1.smt2 --count-tuple'.format(args.bound)
    out, err = shell.runcmd(cmd)
    if args.verbose:
        print(out, err)

    # Parse ABC output into a dictionary
    abc_result = get_abc_result_line(out,err)
    abc_count = int(abc_result['count'])
    abc_time = float(abc_result['solve_time']) + float(abc_result['count_time'])

    # output path, Z3
    print('|[{}/{}]({}/{})|{}|{}|{}|{}|'.format(path, policy, path, policy, z3_count, z3_time, abc_count, abc_time))
    print(result)

for dir in os.listdir(single_policy_dir):
    path = os.fsdecode(single_policy_dir) + os.fsdecode(dir)
    for file in os.listdir(path):
        policy = os.fsdecode(file)
        if policy.endswith('.json'):
            call_solvers(path, policy)
