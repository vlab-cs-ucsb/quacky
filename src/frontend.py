# Functions for frontend (i.e. extracting policy model from policies).

import json
import sys

def validate_args(args):
    """
    Validate arguments to translator.

    Args:
        args (<class 'argparse.Namespace'>): arguments

    Returns:
        tuple: policies (policy1, policy2)
    """

    # AWS
    if args.policy1:
        policy1 = json.loads(open(args.policy1, 'r').read())
        policy2 = None

        if args.policy2:
            policy2 = json.loads(open(args.policy2, 'r').read())

        return (policy1, policy2)

    # Azure
    elif args.role_definitions and args.role_assignment1:
        role_definitions = json.loads(open(args.role_definitions, 'r').read())
        role_assignment1 = json.loads(open(args.role_assignment1, 'r').read())
        role_assignment2 = None

        if args.role_assignment2:
            role_assignment2 = json.loads(open(args.role_assignment2, 'r').read())

        return azure2policy(role_definitions, role_assignment1, role_assignment2)

    # GCP
    elif args.roles and args.role_binding1:
        roles = json.loads(open(args.roles, 'r').read())
        role_binding1 = json.loads(open(args.role_binding1, 'r').read())
        role_binding2 = None

        if args.role_binding2:
            role_binding2 = json.loads(open(args.role_binding2, 'r').read())

        return gcp2policy(roles, role_binding1, role_binding2)

    # Unsupported
    else:
        print('Invalid args! Use -h for help.')
        sys.exit(1)

def azure2policy(role_definitions, role_assignment1, role_assignment2 = None):
    """
    Join Azure role definitions and role assignments into policies

    Args:
        role_definitions (dict): role definitions
        role_assignment1 (dict): role assignment 1
        role_assignment2 (dict, optional): role assignment 2. Defaults to None.

    Returns:
        tuple: policies (policy1, policy2)
    """

    try:
        if not role_assignment2:
            return (azure2policy_helper(role_definitions, role_assignment1),
                    None)
        else:
            return (azure2policy_helper(role_definitions, role_assignment1),
                    azure2policy_helper(role_definitions, role_assignment2))
    
    except:
       print('Invalid Azure role definitions or role assignment(s).')
       sys.exit(1)

def azure2policy_helper(role_definitions, role_assignment):
    """
    Join Azure role definitions and role assignment into a policy.
    Visit both and join on role ID.

    Args:
        role_definitions (dict): role definitions
        role_assignment (dict): role assignment

    Returns:
        dict: policy
    """

    statements = []
        
    for ra in role_assignment:
        for rd in role_definitions:
            if ra['properties']['roleDefinitionId'] == rd['Id']:
                
                statement = {
                    'Id': rd['Id'],
                    'Effect': 'Allow',
                    'Principal': ra['properties']['principalId'],
                    'Action': [a.lower() for a in rd['Actions'] + rd['DataActions']],
                    'Resource': [ra['scope'].lower() + '/*']
                }

                if len(rd['NotActions'] + rd['NotDataActions']) > 0:
                    statement['NotAction']: [a.lower() for a in rd['NotActions'] + rd['NotDataActions']]

                if ra['scope'].count('/') > 6:
                    statement['Resource'].append(ra['scope'].lower())
                
                if 'condition' in ra['properties']:
                    statement['Condition'] = ra['properties']['condition']

                statements.append(statement)
        
    return {'Version': 'azure', 'Statement': statements}

def gcp2policy(roles, role_binding1, role_binding2 = None):
    """
    Join GCP roles and role bindings into policies

    Args:
        roles (dict): roles
        role_binding1 (dict): role binding 1
        role_binding2 (dict, optional): role binding 2. Defaults to None.

    Returns:
        tuple: policies (policy1, policy2)
    """

    # try:
    if not role_binding2:
        return (gcp2policy_helper(roles, role_binding1),
                None)
    else:
        return (gcp2policy_helper(roles, role_binding1),
                gcp2policy_helper(roles, role_binding2))
    
    # except:
        print('Invalid GCP roles or role binding(s).')
        sys.exit(1)

def gcp2policy_helper(roles, role_binding):
    """
    Join GCP roles and role binding into a policy.
    Visit both and join on role ID.

    Args:
        roles (dict): roles
        role_binding (dict): role bindings

    Returns:
        dict: policy
    """

    statements = []

    for rb in role_binding['bindings']:
        for rd in roles:
            if rb['role'] == rd['name']:
                
                statement = {
                    'Id': rd['title'],
                    'Effect': 'Allow',
                    'Principal': rb['members'],
                    'Action': [a.lower() for a in rd['includedPermissions']],
                    'Resource': [rb['level'].lower() + '/*']
                }

                if rb['level'].count('/') > 2:
                    statement['Resource'].append(rb['level'].lower())

                if 'condition' in rb:
                    statement['Condition'] = rb['condition']['expression'].lower()

                statements.append(statement)

    return {'Version': 'gcp', 'Statement': statements}

def sanitize_and_wrap(policy1, policy2 = None):
    """
    Sanitize and wrap policies.

    Args:
        policy1 (dict): policy 1
        policy2 (dict): policy 2

    Returns:
        obj: sanitized, wrapped policy
    """
    obj = sanitize_helper(policy1)
    
    if policy2:
	    policy2 = sanitize_helper(policy2)
	    obj = {'policies': [obj, policy2]}

    return obj

def sanitize_helper(obj):
    """
    Recursively sanitize a policy. Modify keys.

    Args:
        obj (dict): policy

    Returns:
        dict: sanitized policy
    """

    if type(obj) in [bool, int, str]:
        obj = [obj]

    elif type(obj) == dict:
        for i in obj:
            if i not in ['Effect', 'Version', 'Sid']:
                obj[i] = sanitize_helper(obj[i])
            elif i == 'Version':
                if obj[i] not in ['azure', 'gcp']:
                    obj[i] = 'aws'

    elif type(obj) == list:
        for i in range(len(obj)):
            if type(obj[i]) not in [bool, int, str]:
                obj[i] = sanitize_helper(obj[i])

    return obj