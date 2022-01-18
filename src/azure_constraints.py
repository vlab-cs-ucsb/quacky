# Functions for building Azure resource type constraints and action encoding (online)

from utilities import disjunction_to_ranges
import json
import re

# Azure scope format (PCRE)
scope_format = '''
/subscriptions
    /[0-9a-f]{{8}}\-[0-9a-f]{{4}}\-[0-9a-f]{{4}}\-[0-9a-f]{{4}}\-[0-9a-f]{{12}}
        /resourcegroups
            /[A-Za-z0-9_+=,.@\-]+
                /providers
                    /{}
                        /{}
                            /[A-Za-z0-9_+=,.@\-]+
'''
scope_format = scope_format.replace(' ', '')
scope_format = scope_format.replace('\n', '')

# Azure scope format (SMT-LIB)
scope_smt_lib_format = '''
(re.++
(str.to.re "/subscriptions/")
((_ re.loop 8 8) (re.union (re.range "0" "9") (re.range "a" "f")))
(str.to.re "-")
((_ re.loop 4 4) (re.union (re.range "0" "9") (re.range "a" "f")))
(str.to.re "-")
((_ re.loop 4 4) (re.union (re.range "0" "9") (re.range "a" "f")))
(str.to.re "-")
((_ re.loop 4 4) (re.union (re.range "0" "9") (re.range "a" "f")))
(str.to.re "-")
((_ re.loop 12 12) (re.union (re.range "0" "9") (re.range "a" "f")))
(str.to.re "/resourcegroups/")
(re.+ (re.union (re.range "A" "Z") (re.range "a" "z") (re.range "0" "9") (str.to.re "_") (str.to.re "+") (str.to.re "=") (str.to.re ",") (str.to.re ".") (str.to.re "@") (str.to.re "-")))
(str.to.re "/providers/")
(str.to.re "{}") 
(str.to.re "/")
(str.to.re "{}")
(str.to.re "/")
(re.+ (re.union (re.range "A" "Z") (re.range "a" "z") (re.range "0" "9") (str.to.re "_") (str.to.re "+") (str.to.re "=") (str.to.re ",") (str.to.re ".") (str.to.re "@") (str.to.re "-"))))
'''
scope_smt_lib_format = ' '.join(scope_smt_lib_format.split('\n'))
scope_smt_lib_format = scope_smt_lib_format.lstrip()

def relevant_types(_json, action):
    """
    Infers relevant resource types from an Azure action.

    Args:
        _json (dict): action/resource type mapping, as JSON
        action (string): action, possibly with wildcard

    Returns:
        set: relevant resource types
    """

    provider = action.split('/')[0]

    if provider not in _json:
        return None

    # Convert action to regex pattern
    pattern = action
    pattern = pattern.replace('.', '\.')
    pattern = pattern.replace('/', '\/')
    pattern = pattern.replace('*', '.*')
    pattern = re.compile(pattern)

    types = set()

    for resource_type in _json[provider]:
        for action in _json[provider][resource_type]:
            if re.match(pattern, '{}/{}/{}'.format(provider, resource_type, action)):
                types.add(resource_type)

    return types

def azure_type_constraints(actions, smt_lib = False, enc = False):
    """
    Builds Azure resource type constraints

    Args:
        actions (list): actions
        smt_lib (bool, optional): use SMT-LIB syntax. Defaults to False.
        enc (bool, optional): use action encoding. Defaults to False.

    Returns:
        str: SMT encoding of resource type constraints
    """

    # Files with offline action encoding
    actions_json = json.loads(open('offline/azure/actions.json', 'r').read())
    data_actions_json = json.loads(open('offline/azure/data_actions.json', 'r').read())
    encoding_actions_json = json.loads(open('offline/azure/encoding_actions.json', 'r').read())
    encoding_data_actions_json = json.loads(open('offline/azure/encoding_data_actions.json', 'r').read())
    
    # Infer the relevant resource types
    actions_types = {}
    data_actions_types = {}
    
    for action in actions:
        if action == '*':
            print('Action is *; no point in this.')
            return ''

        provider = action.split('/')[0]

        types = relevant_types(actions_json, action)
        if types and provider not in actions_types:
            actions_types[provider] = types
        elif types and provider in actions_types:
            actions_types[provider].update(types)
        
        types = relevant_types(data_actions_json, action)
        if types and provider not in data_actions_types:
            data_actions_types[provider] = types
        elif types and provider in data_actions_types:
            data_actions_types[provider].update(types)

    smt = ''

    # Add a constraint on the min. and max. numbers used for encodings
    if enc:
        lo = encoding_actions_json['_lo']
        hi = encoding_data_actions_json['_hi']

        if smt_lib:
            smt += '(assert (and (>= (str.to_int action) {}) (<= (str.to_int action) {})))\n'.format(int(lo), int(hi))
            smt += '(assert (str.in.re action ((_ re.loop 5 5) (re.range "0" "9"))))\n'
        else:
            smt += '(assert (and (>= action "{}") (<= action "{}")))\n'.format(lo, hi)
            smt += '(assert (in action /[0-9]{5,5}/))\n'

    smt += '(assert (or'

    # Add constraints on action/resource type pairs
    for provider in actions_types:
        for resource_type in actions_types[provider]:

            smt += ' (and'

            if smt_lib:
                scope = scope_smt_lib_format.format(provider, resource_type)
                scope = scope.replace('//', '/')
                
                smt += ' (str.in.re resource {})'.format(scope)
            
            else:
                scope = scope_format.format(provider.replace('.', '\.'), resource_type.replace('.', '\.'))
                scope = scope.replace('//', '/')
                scope = scope.replace('/', '\\/')
            
                smt += ' (in resource /{}/)'.format(scope)
            
            if enc:
                lo = min(encoding_actions_json[provider][resource_type].values())
                hi = max(encoding_actions_json[provider][resource_type].values())

                if smt_lib:
                    smt += ' (and (>= (str.to_int action) {}) (<= (str.to_int action) {}))'.format(int(lo), int(hi))
                else:
                    smt += ' (and (>= action "{}") (<= action "{}"))'.format(lo, hi)

            else:
                smt += ' (or'
            
                for action in actions_json[provider][resource_type]:
                    if resource_type == '':
                        smt += ' (= action "{}/{}")'.format(provider, action)
                    else:
                        smt += ' (= action "{}/{}/{}")'.format(provider, resource_type, action)

                smt += ')'

            smt += ')'
    
    # Add constraints on data action/resource type pairs
    for provider in data_actions_types:
        for resource_type in data_actions_types[provider]:

            smt += ' (and'

            if smt_lib:
                scope = scope_smt_lib_format.format(provider, resource_type)
                scope = scope.replace('//', '/')
                
                smt += ' (str.in.re resource (re.++ {} (str.to.re "/") (re.* re.allchar)))'.format(scope)
            
            else:
                scope = scope_format.format(provider.replace('.', '\.'), resource_type.replace('.', '\.'))
                scope = scope.replace('//', '/')
                scope = scope.replace('/', '\\/')
            
                smt += ' (in resource /{}\/.*/)'.format(scope)

            if enc:
                lo = min(encoding_data_actions_json[provider][resource_type].values())
                hi = max(encoding_data_actions_json[provider][resource_type].values())

                if smt_lib:
                    smt += ' (and (>= (str.to_int action) {}) (<= (str.to_int action) {}))'.format(int(lo), int(hi))
                else:
                    smt += ' (and (>= action "{}") (<= action "{}"))'.format(lo, hi)

            else:
                smt += ' (or'
            
                for action in data_actions_json[provider][resource_type]:
                    if resource_type == '':
                        smt += ' (= action "{}/{}")'.format(provider, action)
                    else:
                        smt += ' (= action "{}/{}/{}")'.format(provider, resource_type, action)

                smt += ')'
        
            smt += ')'
    
    smt += '))'

    return smt

def azure_action_encoding(action, smt_lib = False):
    """
    Get the numeric encoding for an Azure action

    Args:
        action (str): action
        smt_lib (bool, optional): use SMT-LIB syntax. Defaults to False.

    Returns:
        str: SMT encoding
    """

    # Files with offline action encoding
    encoding_actions_json = json.loads(open('offline/azure/encoding_actions.json', 'r').read())
    encoding_data_actions_json = json.loads(open('offline/azure/encoding_data_actions.json', 'r').read())
    
    smt = ''

    if action == '*':
        lo = encoding_actions_json['_lo']
        hi = encoding_data_actions_json['_hi']

        if smt_lib:
            smt += ' (and (>= (str.to_int action) {}) (<= (str.to_int action) {}))'.format(int(lo), int(hi))
        else:
            smt += ' (and (>= action "{}") (<= action "{}"))'.format(lo, hi)

        return smt

    pattern = '^' + action + '$'
    pattern = pattern.replace('*', '.*').replace('?', '.?')

    # get actions and respective encodings
    disjunction = []
    disjunction += [v for k, v in encoding_actions_json['_all'].items() if re.match(pattern, k)]
    disjunction += [v for k, v in encoding_data_actions_json['_all'].items() if re.match(pattern, k)]

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