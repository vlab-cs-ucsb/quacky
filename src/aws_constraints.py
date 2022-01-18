# Functions for building AWS resource type constraints and action encoding (online)

from utilities import disjunction_to_ranges
import json
import re

def aws_type_constraints(namespaces, smt_lib = False, enc = False):
    """
    Builds AWS resource type constraints

    Args:
        namespaces (set): namespaces, or services
        smt_lib (bool, optional): use SMT-LIB syntax. Defaults to False.
        enc (bool, optional): use action encoding. Defaults to False.

    Returns:
        str: SMT encoding of resource type constraints
    """

    smt = ''

    # Only use valid namespaces if none are specified
    if '*' in namespaces:
        namespaces = json.loads(open('offline/aws/namespaces.json', 'r').read())
        namespaces = [namespace for namespace, is_valid in namespaces.items() if is_valid == True]

    if len(namespaces) == 0:
        return ''

    # Add a constraint on the min. and max. numbers used for encodings
    if enc:
        encoding_json = json.loads(open('offline/aws/encoding.json', 'r').read())
        lo = encoding_json['_lo']
        hi = encoding_json['_hi']

        if smt_lib:
            smt_json = json.loads(open('offline/aws/constraints_enc_z3.json', 'r').read())
            smt += '(assert (and (>= (str.to_int action) {}) (<= (str.to_int action) {})))\n'.format(int(lo), int(hi))
            smt += '(assert (str.in.re action ((_ re.loop 5 5) (re.range "0" "9"))))\n'
        else:
            smt_json = json.loads(open('offline/aws/constraints_enc.json', 'r').read())
            smt += '(assert (and (>= action "{}") (<= action "{}")))\n'.format(lo, hi)
            smt += '(assert (in action /[0-9]{5,5}/))\n'
    else:
        if smt_lib:
            smt_json = json.loads(open('offline/aws/constraints_z3.json', 'r').read())
        else:
            smt_json = json.loads(open('offline/aws/constraints.json', 'r').read())

    smt += '(assert (or'
    
    for namespace in namespaces:
        smt += ' ' + smt_json[namespace]

    smt += '))\n\n'

    return smt

def aws_action_encoding(action, smt_lib):
    """
    Get the numeric encoding for an AWS action

    Args:
        action (str): action
        smt_lib (bool, optional): use SMT-LIB syntax. Defaults to False.

    Returns:
        str: SMT encoding
    """

    # Files with offline action encoding
    encoding_json = json.loads(open('offline/aws/encoding.json', 'r').read())

    namespace = action.split(':')[0]
    pattern = action.split(':')[1]

    smt = ''

    if pattern == '*':
        lo = encoding_json[namespace]['_lo']
        hi = encoding_json[namespace]['_hi']

        if smt_lib:
            smt += ' (and (>= (str.to_int action) {}) (<= (str.to_int action) {}))'.format(int(lo), int(hi))
        else:
            smt += ' (and (>= action "{}") (<= action "{}"))'.format(lo, hi)

        return smt

    pattern = '^' + action + '$'
    pattern = pattern.replace('*', '.*').replace('?', '.?')

    # get actions and respective encodings
    actions = [action for action in encoding_json['_all'] if re.match(pattern, action)]
    
    disjunction = []
    for action in actions:
        disjunction += [n for n in encoding_json['_all'][action]]

    ranges = disjunction_to_ranges(disjunction)

    if len(ranges) > 1:
        smt += ' (or'
    
    # Create range constraints
    for r in ranges:
        if type(r) == tuple:
            lo = r[0]
            hi = r[1]

            if smt_lib:
                smt += ' (and (>= (str.to_int action) {}) (<= (str.to_int action) {}))'.format(int(lo), int(hi))
            else:
                smt += ' (and (>= action "{}") (<= action "{}"))'.format(lo, hi)
        
        else:
            if smt_lib:
                smt += ' (= (str.to_int action) {})'.format(int(r))
            else:
                smt += ' (= action "{}")'.format(r)

    if len(ranges) > 1:
        smt += ')'

    return smt