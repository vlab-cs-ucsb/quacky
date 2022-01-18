# Script to mutate policies. See paper for technical details.

import argparse as ap
import json
import os
import random
import shutil
from itertools import chain, combinations, product

parser = ap.ArgumentParser(description="Mutate AWS IAM policies")
parser.add_argument('-d', '--dir', help='Policy Directory', required=True)
args = parser.parse_args()

def powerset(S):
    """
    Get the power set P(S) of S

    Args:
        S (list): a set

    Returns:
        list: power set P(S)
    """
    return list(chain.from_iterable(combinations(S, r) for r in range(len(S) + 1)))

def change_effect(statement):
    """
    Type 1 mutation: change effect on actions, resources

    Args:
        statement (str): statement

    Returns:
        str: mutated statement
    """

    statement = json.loads(statement)

    if statement['Effect'] == 'Deny':
        if 'Resource' in statement.keys():
            statement['NotResource'] = statement.pop('Resource')
        elif 'NotResource' in statement.keys():
            statement['Resource'] = statement.pop('NotResource')
        
        if 'Action' in statement.keys():
            statement['NotAction'] = statement.pop('Action')
        elif 'NotAction' in statement.keys():
            statement['Action'] = statement.pop('NotAction')
    
    return json.dumps(statement)
        
def remove_conditions(statement):
    """
    Type 2 mutation: remove condition element

    Args:
        statement (str): statement

    Returns:
        str: mutated statement
    """

    statement = json.loads(statement)

    if 'Condition' in statement.keys():
        statement.pop('Condition')
    
    return json.dumps(statement)

def remove_lists(statement):
    """
    Type 3 mutation: convert list into wildcard

    Args:
        statement (str): statement

    Returns:
        str: mutated statement
    """

    statement = json.loads(statement)
    key = ''

    if 'Resource' in statement.keys():
        key = 'Resource'
    elif 'NotResource' in statement.keys():
        key = 'NotResource'
    
    if type(statement[key]) == list:
        temp = statement[key][0].split(':')
        if len(temp) > 1:
            statement[key] = ':'.join(temp[0:-1]) + ':*'
    
    if 'Action' in statement.keys():
        key = 'Action'
    elif 'NotAction' in statement.keys():
        key = 'NotAction'

    if type(statement[key]) == list:
        statement[key] = statement[key][0].split(':')[0] + ':*'
    
    return json.dumps(statement)

def mutate_policy(path, policy):
    """
    Mutates a policy in a directory

    Args:
        path (str): policy directory
        policy (str): policy filename
    """

    obj = open(os.path.join(path, policy), 'r').read()
    obj_json = json.loads(obj)
    statements = obj_json['Statement']
    powersets_of_mutations = []
    
    for i in range(len(statements)):
        statements[i] = json.dumps(statements[i])
        # applicable mutations for statement
        mutations = [change_effect]
        
        if 'Condition' in statements[i]:
            mutations.append(remove_conditions)
        if '[' in statements[i] and ']' in statements[i]:
            mutations.append(remove_lists)
        
        powerset_of_mutations = powerset(mutations)
        powersets_of_mutations.append(powerset_of_mutations)

    indices_in_powersets = [
        [i for i in range(len(PS))] for PS in powersets_of_mutations]

    if len(indices_in_powersets) <= 2:
        tuples_of_lengths = product(*indices_in_powersets)

        for t in tuples_of_lengths:
            mutated_statements = []
            
            for i in range(len(t)):
                mutated_statement = statements[i]  # mutated policy object
                mutations = powersets_of_mutations[i][t[i]]

                for mutation in mutations:
                    # try unconditionally added mutations
                    mutated_statement = mutation(mutated_statement)

                mutated_statements.append(json.loads(mutated_statement))

            obj = {'Statement': mutated_statements}
            filename = str(t)
            filename = filename.replace('(', '')
            filename = filename.replace(')', '')
            filename = filename.replace(',', '_')
            filename = filename.replace(' ', '')
            file = open('mutations/{}/{}/{}'.format(path, policy.replace('.json',''), filename + '.json').replace('"', ''), 'w')
            file.write(json.dumps(obj, indent=4))
            file.close()

# args.dir : "s3/exp_single"
for dir in os.listdir(args.dir):
    path = os.fsdecode(args.dir) + '/' + os.fsdecode(dir)
    # path : "s3/exp_single/s3_iam_user_cannot_create_folder_through_console"
    for file in os.listdir(path):
        policy = os.fsdecode(file)

        # create destination directory
        if policy.endswith('.json'):
            try:
                shutil.rmtree('mutations/{}/{}'.format(path,
                                                       policy.replace('.json', '')))
                print('Remove: mutations/{}/{}'.format(path,
                                                       policy.replace('.json', '')))
            except:
                pass
            try:
                os.makedirs('mutations/{}/{}'.format(path,
                                                     policy.replace('.json', '')))
                print('Make: mutations/{}/{}'.format(path,
                                                     policy.replace('.json', '')))
            except:
                pass

            mutate_policy(path, policy)
