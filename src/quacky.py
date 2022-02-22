from frontend import validate_args
from tabulate import tabulate
from translator import call_translator
from utilities import *
from utils.Shell import Shell

import argparse as ap
import math

def call_abc(args):
    shell = Shell()
    policy1, policy2 = validate_args(args)

    # Call ABC on formula 1
    cmd = 'abc -bs {} -v 0 -i {}_1.smt2 --precise --count-tuple'.format(args.bound, args.output)
    if args.variable:
        cmd += ' --count-variable principal,action,resource'
    
    out, err = shell.runcmd(cmd)
    if args.verbose:
        print(out, err)

    result1 = get_abc_result_line(out, err)

    # Format results table
    table1 = [
        ['Solve Time (ms)', result1['solve_time']],
        ['Satisfiability', result1['is_sat']]
    ]

    if 'count' in result1 and int(result1['count']) > 0:
        table1 += [
            ['Count Time (ms)', result1['count_time']],
            ['lg(requests)', math.log2(int(result1['count']))]
        ]
    else:
        table1.append(['requests', 0])

    for k, v in result1['var'].items():
        if int(v['count']) > 0:
            table1.append(['lg({})'.format(k), math.log2(int(v['count']))])
        else:
            table1.append([k, 0])
    
    print('Policy 1 ⇏ Policy 2' if policy2 else 'Policy 1')
    print(tabulate(table1, tablefmt = 'fancy_grid'))
    print()

    if not policy2:
        return

    # Call ABC on formula 2
    cmd = 'abc -bs {} -v 0 -i {}_2.smt2 --precise --count-tuple'.format(args.bound, args.output)
    if args.variable:
        cmd += ' --count-variable principal,action,resource'
        
    out, err = shell.runcmd(cmd)
    if args.verbose:
        print(out, err)

    result2 = get_abc_result_line(out, err)
    
    # Format results table
    table2 = [
        ['Solve Time (ms)', result2['solve_time']],
        ['Satisfiability', result2['is_sat']]
    ]

    if 'count' in result2 and int(result2['count']) > 0:
        table2 += [
            ['Count Time (ms)', result2['count_time']], 
            ['lg(requests)', math.log2(int(result2['count']))]
        ]
    else:
        table2.append(['requests', 0])

    for k, v in result2['var'].items():
        if int(v['count']) > 0:
            table2.append(['lg({})'.format(k), math.log2(int(v['count']))])
        else:
            table2.append([k, 0])
    
    print('Policy 2 ⇏ Policy 1')
    print(tabulate(table2, tablefmt = 'fancy_grid'))
    print()

    if result1['is_sat'] == 'SAT' and result2['is_sat'] == 'SAT':
        print('Policy 1 and Policy 2 do not subsume each other.')
    elif result1['is_sat'] == 'SAT' and result2['is_sat'] == 'UNSAT':
        print('Policy 1 is more permissive than Policy 2.')
    elif result1['is_sat'] == 'UNSAT' and result2['is_sat'] == 'SAT':
        print('Policy 1 is less permissive than Policy 2.')
    else:
        print('Policy 1 and Policy 2 are equivalent.')

if __name__ == '__main__':
    parser = ap.ArgumentParser(description = 'Quantitatively analyze permissiveness of access control policies')
    parser.add_argument('-p1' , '--policy1'         , help = 'policy 1 (AWS)'               , required = False)
    parser.add_argument('-p2' , '--policy2'         , help = 'policy 2 (AWS)'               , required = False)
    parser.add_argument('-rd' , '--role-definitions', help = 'role definitions (Azure)'     , required = False)
    parser.add_argument('-ra1', '--role-assignment1', help = 'role assignment 1 (Azure)'    , required = False)
    parser.add_argument('-ra2', '--role-assignment2', help = 'role assignment 2 (Azure)'    , required = False)
    parser.add_argument('-r'  , '--roles'           , help = 'roles (GCP)'                  , required = False)
    parser.add_argument('-rb1', '--role-binding1'   , help = 'role binding 1 (GCP)'         , required = False)
    parser.add_argument('-rb2', '--role-binding2'   , help = 'role binding 2 (GCP)'         , required = False)
    # parser.add_argument('-d'  , '--domain'          , help = 'domain file (not supported)'  , required = False)
    parser.add_argument('-o'  , '--output'          , help = 'output file'                  , required = False, default = 'output')
    parser.add_argument('-s'  , '--smt-lib'         , help = 'use SMT-LIB syntax'           , required = False, action = 'store_true')
    parser.add_argument('-e'  , '--enc'             , help = 'use action encoding'          , required = False, action = 'store_true')
    parser.add_argument('-c'  , '--constraints'     , help = 'use resource type constraints', required = False, action = 'store_true')
    parser.add_argument('-b'  , '--bound'           , help = 'bound'                        , required = True , default = 100)
    parser.add_argument('-f'  , '--variable'        , help = 'count all variables'          , required = False, action = 'store_true')
    parser.add_argument('-v', '--verbose', help = 'Verbose', required = False, action = 'store_true')
    args = parser.parse_args()

    call_translator(args)
    call_abc(args)
