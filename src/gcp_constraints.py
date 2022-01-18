# Functions for building GCP resource type constraints and action encoding (online)

from utilities import disjunction_to_ranges
import json
import re

# GCP scope format (PCRE)
scope_format = '''
/[A-Za-z0-9_+=,.@\-]+
    /[A-Za-z0-9_+=,.@\-]+
        /[A-Za-z0-9_+=,.@\-]+
            /{}/[A-Za-z0-9_+=,.@\-]+
'''
scope_format = scope_format.replace(' ', '')
scope_format = scope_format.replace('\n', '')

# GCP scope format (SMT-LIB)
scope_smt_lib_format = '''
(re.++
(str.to.re "/")
(re.+ (re.union (re.range "A" "Z") (re.range "a" "z") (re.range "0" "9") (str.to.re "_") (str.to.re "+") (str.to.re "=") (str.to.re ",") (str.to.re ".") (str.to.re "@") (str.to.re "-")))
(str.to.re "/")
(re.+ (re.union (re.range "A" "Z") (re.range "a" "z") (re.range "0" "9") (str.to.re "_") (str.to.re "+") (str.to.re "=") (str.to.re ",") (str.to.re ".") (str.to.re "@") (str.to.re "-")))
(str.to.re "/")
(re.+ (re.union (re.range "A" "Z") (re.range "a" "z") (re.range "0" "9") (str.to.re "_") (str.to.re "+") (str.to.re "=") (str.to.re ",") (str.to.re ".") (str.to.re "@") (str.to.re "-")))
(str.to.re "/")
(str.to.re "{}")
(str.to.re "/")
(re.+ (re.union (re.range "A" "Z") (re.range "a" "z") (re.range "0" "9") (str.to.re "_") (str.to.re "+") (str.to.re "=") (str.to.re ",") (str.to.re ".") (str.to.re "@") (str.to.re "-"))))
'''
scope_smt_lib_format = ' '.join(scope_smt_lib_format.split('\n'))
scope_smt_lib_format = scope_smt_lib_format.lstrip()

def relevant_types(_json, action):
    """
    Infers relevant resource types from a GCP action.

    Args:
        _json (dict): action/resource type mapping, as JSON
        action (string): action, possibly with wildcard

    Returns:
        set: relevant resource types
    """

    pattern = action
    pattern = pattern.replace('.', '\.')
    pattern = pattern.replace('/', '\/')
    pattern = pattern.replace('*', '.*')
    pattern = re.compile(pattern)

    types = set()

    for resource_type in _json:
        for action in _json[resource_type]:
            if re.match(pattern, action):
                types.add(resource_type)

    return types

def gcp_type_constraints(actions, smt_lib = False, enc = False):
    """
    Builds GCP resource type constraints

    Args:
        actions (list): actions
        smt_lib (bool, optional): use SMT-LIB syntax. Defaults to False.
        enc (bool, optional): use action encoding. Defaults to False.

    Returns:
        str: SMT encoding of resource type constraints
    """

    # Files with offline action encoding
    actions_json = json.loads(open('offline/gcp/actions.json', 'r').read())
    encoding_actions_json = json.loads(open('offline/gcp/encoding_actions.json', 'r').read())
    
    # Infer relevant resource types
    types = set()

    for action in actions:
        if action == '*':
            print('Action is *; no point in this.')
            return ''

        types.update(relevant_types(actions_json, action))

    smt = ''

    # Add a constraint on the min. and max. numbers used for encodings
    if enc:
        lo = encoding_actions_json['_lo']
        hi = encoding_actions_json['_hi']

        if smt_lib:
            smt += '(assert (and (>= (str.to_int action) {}) (<= (str.to_int action) {})))\n'.format(int(lo), int(hi))
            smt += '(assert (str.in.re action ((_ re.loop 3 3) (re.range "0" "9"))))\n'
        else:
            smt += '(assert (and (>= action "{}") (<= action "{}")))\n'.format(lo, hi)
            smt += '(assert (in action /[0-9]{3,3}/))\n'

    smt += '(assert (or'

    # Add constraints on action/resource type pairs
    for resource_type in types:

        smt += ' (and'

        if smt_lib:
            scope = scope_smt_lib_format.format(resource_type)
            
            smt += ' (str.in.re resource {})'.format(scope)
        
        else:
            scope = scope_format.format(resource_type)
            scope = scope.replace('//', '/')
            scope = scope.replace('/', '\\/')
        
            smt += ' (in resource /{}/)'.format(scope)
        
        if enc:
            lo = min(encoding_actions_json[resource_type].values())
            hi = max(encoding_actions_json[resource_type].values())

            if smt_lib:
                smt += ' (and (>= (str.to_int action) {}) (<= (str.to_int action) {}))'.format(int(lo), int(hi))
            else:
                smt += ' (and (>= action "{}") (<= action "{}"))'.format(lo, hi)

        else:
            smt += ' (or'
        
            for action in actions_json[resource_type]:
                smt += ' (= action "{}")'.format(action)

            smt += ')'

        smt += ')'
    
    smt += '))'

    return smt

def gcp_action_encoding(action, smt_lib):
    """
    Get the numeric encoding for a GCP action

    Args:
        action (str): action
        smt_lib (bool, optional): use SMT-LIB syntax. Defaults to False.

    Returns:
        str: SMT encoding
    """

    # Files with offline action encoding
    encoding_actions_json = json.loads(open('offline/gcp/encoding_actions.json', 'r').read())
    
    smt = ''

    if action == '*':
        lo = encoding_actions_json['_lo']
        hi = encoding_actions_json['_hi']

        if smt_lib:
            smt += ' (and (>= (str.to_int action) {}) (<= (str.to_int action) {}))'.format(int(lo), int(hi))
        else:
            smt += ' (and (>= action "{}") (<= action "{}"))'.format(lo, hi)

        return smt

    pattern = '^' + action + '$'
    pattern = pattern.replace('*', '.*').replace('?', '.?')

    # get actions and respective encodings
    disjunction = [v for k, v in encoding_actions_json['_all'].items() if re.match(pattern, k)]

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