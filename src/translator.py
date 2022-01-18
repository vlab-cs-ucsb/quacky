# Entry point for translation of policies to SMT-LIB.
# This script does not do model counting or constraint solving.

from frontend import *
from backend import *
from utilities import *

import argparse as ap
import json

def call_translator(args):
    policy1, policy2 = validate_args(args)
    obj = sanitize_and_wrap(policy1, policy2)

    # Add a domain from a domain file
    domain = dict()

    """ 
    if args.domain:
        domain = json.loads(open(args.domain, 'r').read())
        domain = sanitize_helper(domain)
    """

    # Create a SMT formula in backend
    body = visit_policy_model(
        obj, 
        domain, False, args.smt_lib, args.enc, args.constraints)

    # Write SMT formula to file
    if not policy2:
        # Write SMT formula to file
        file = open(args.output + '_1.smt2', 'w')
        file.write(header() + body + footer('p0'))
        file.close()

    else:
        file1 = open(args.output + '_1.smt2', 'w')
        file1.write(header() + body + footer('p0', 'p1'))
        file1.close()
        file2 = open(args.output + '_2.smt2', 'w')
        file2.write(header() + body + footer('p1', 'p0'))
        file2.close()

    """ 
    # Translate domain
    if args.domain:
        # Convert domain into a valid policy
        domain.update({'Effect': 'Allow'})
        domain.pop('Condition', None)

        body = visit_policy_model(
            {'Statement': [domain]}, 
            dict(), True, args.smt_lib, args.enc, args.constraints)
    else:
        body = visit_policy_model(
            {'Statement': {'Effect': 'Allow', 'Principal': '*'}}, 
            dict(), True, args.smt_lib, args.enc, args.constraints)
        
    # Write domain formula to file
    file = open(args.output + '_0.smt2', 'w')
    file.write(header() + body + footer('p0'))
    file.close()
    """

if __name__ == '__main__':
    # Parse arguments
    parser = ap.ArgumentParser(description = 'Translate access control policies to SMT formulas')
    parser.add_argument('-p1' , '--policy1'         , help = 'policy 1 (AWS)'               , required = False)
    parser.add_argument('-p2' , '--policy2'         , help = 'policy 2 (AWS)'               , required = False)
    parser.add_argument('-rd' , '--role-definitions', help = 'role definitions (Azure)'     , required = False)
    parser.add_argument('-ra1', '--role-assignment1', help = 'role assignment 1 (Azure)'    , required = False)
    parser.add_argument('-ra2', '--role-assignment2', help = 'role assignment 2 (Azure)'    , required = False)
    parser.add_argument('-r'  , '--roles'           , help = 'roles (GCP)'                  , required = False)
    parser.add_argument('-rb1', '--role-binding1'   , help = 'role binding 1 (GCP)'         , required = False)
    parser.add_argument('-rb2', '--role-binding2'   , help = 'role binding 2 (GCP)'         , required = False)
    # parser.add_argument('-d'  , '--domain'          , help = 'domain file (not supported)'  , required = False)
    parser.add_argument('-o'  , '--output'          , help = 'output file'                  , required = False, default='output')
    parser.add_argument('-s'  , '--smt-lib'         , help = 'use SMT-LIB syntax'           , required = False, action = 'store_true')
    parser.add_argument('-e'  , '--enc'             , help = 'use action encoding'          , required = False, action = 'store_true')
    parser.add_argument('-c'  , '--constraints'     , help = 'use resource type constraints', required = False, action = 'store_true')
    args = parser.parse_args()

    call_translator(args)