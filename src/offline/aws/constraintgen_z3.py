# builds AWS resource type constraints using SMT-LIB syntax (offline)

import json
import re

# actions and corresponding resource types
actions_json = json.loads(open('actions.json', 'r').read())
resources_json = json.loads(open('resources.json', 'r').read())

# custom regex for ARNs and resource types
arn_regex = json.loads(open('arn_regex.json', 'r').read())
resource_regex = json.loads(open('resource_regex_z3.json', 'r').read())

smt_json = {}

# iterate through all services
for namespace in actions_json.keys():
    actions = actions_json[namespace]
    resource_types = resources_json[namespace]

    smt = ''

    if len(resource_types) > 0:
        smt += '(or'
        
        for resource_type in actions:
            smt += ' (and'
        
            # if no resource type specified, use a generic ARN format for that resource type
            if resource_type == '':
                # check if there is a generic ARN in arg_regex.json
                if namespace in arn_regex:
                    resource = arn_regex[namespace]
                    resource_parts = resource.split(':')
                    
                    # substitute in regex representations of ${...}
                    resource_parts[1] = resource_parts[1].replace('${Partition}', '(str.to.re "aws")')
                    resource_parts[3] = resource_parts[3].replace('${Region}', '(re.++ (re.union (re.++ (str.to.re "us") (re.opt (str.to.re "-gov"))) (str.to.re "ap") (str.to.re "ca") (str.to.re "cn") (str.to.re "eu") (str.to.re "sa")) (str.to.re "-") (re.union (str.to.re "central") (re.++ (re.opt (re.union (str.to.re "north") (str.to.re "south"))) (re.opt (re.union (str.to.re "east") (str.to.re "west"))))) (str.to.re "-") (re.range "0" "9") (re.opt (re.range "a" "z")))')
                    resource_parts[4] = resource_parts[4].replace('${Account}', '((_ re.loop 12 12) (re.range "0" "9"))')
                    
                    smt += ' (str.in.re resource'
                    smt += ' (re.++'
                    smt += ' (str.to.re "arn:aws:")'
                    smt += ' (str.to.re "' + namespace + ':")'
                    
                    if not resource_parts[3] == '':
                        smt += ' ' + resource_parts[3]
                    
                    smt += ' (str.to.re ":")'
                    
                    if not resource_parts[4] == '':
                        smt += ' ' + resource_parts[4]
                    
                    smt += ' (str.to.re ":")'
                    
                    if (not resource_parts[5] == '') and (not resource_parts[5] == "\*"):
                        smt += ' (re.++ ' + resource_parts[5] + ')'
                    else:
                        smt += ' (str.to.re "*")'
                    
                    smt += '))'
                
                # if no generic ARN in arg_regex.json, use the regex below
                else:
                    smt += ' (str.in.re resource (re.++ (re.opt (re.++ (str.to.re "arn:aws:") (str.to.re "' + namespace + '") (str.to.re ":") (re.opt (re.++ (re.union (re.++ (str.to.re "us") (re.opt (str.to.re "-gov"))) (str.to.re "ap") (str.to.re "ca") (str.to.re "cn") (str.to.re "eu") (str.to.re "sa")) (str.to.re "-") (re.union (str.to.re "central") (re.++ (re.opt (re.union (str.to.re "north") (str.to.re "south"))) (re.opt (re.union (str.to.re "east") (str.to.re "west"))))) (str.to.re "-") (re.range "0" "9") (re.opt (re.range "a" "z")))) (str.to.re ":") (re.opt ((_ re.loop 12 12) (re.range "0" "9"))) (str.to.re ":"))) (str.to.re "*")))'
            
            # if resource type specified
            else:
                resource_parts = resource_types[resource_type].split(':')
                flag = 0
                
                # parse the resource type expression and create SMT regex to represent the ARN
                for i in range(1, len(resource_parts)):
                    resourceResource = resource_parts[i].split('/')
                    
                    for j in range(len(resourceResource)):
                        if (not ('$' in resourceResource[j])) and (not ('re.' in resourceResource[j])) and (not ('.re' in resourceResource[j])) and (not ('str' in resourceResource[j])):
                            resourceResource[j] = '(str.to.re "'+ resourceResource[j] + '")'   
                    
                    if len(resourceResource) >0 :
                        temp = resourceResource[0]
                        
                        for k in range(1, len(resourceResource)):
                            temp = temp + ' (str.to.re "/")' + resourceResource[k] 
                            flag = 1
                        
                        resource_parts[i] = temp
                    
                    if namespace in resource_regex:
                        for obj, reg_expr in resource_regex[namespace].items():
                            resource_parts[i] = resource_parts[i].replace('${' + obj + '}', reg_expr)
                
                for i in range(1, len(resource_parts)):
                    if i == 3: #replace ${Region}
                        resource_parts[i] = re.sub('\$\{.+\}', '(re.++ (re.union (re.++ (str.to.re "us") (re.opt (str.to.re "-gov"))) (str.to.re "ap") (str.to.re "ca") (str.to.re "cn") (str.to.re "eu") (str.to.re "sa")) (str.to.re "-") (re.union (str.to.re "central") (re.++ (re.opt (re.union (str.to.re "north") (str.to.re "south"))) (re.opt (re.union (str.to.re "east") (str.to.re "west"))))) (str.to.re "-") (re.range "0" "9") (re.opt (re.range "a" "z")))', resource_parts[i], flags = re.DOTALL)
                    if i == 4: # replace ${AccountID}
                        resource_parts[i] = re.sub('\$\{.+\}', '((_ re.loop 12 12) (re.range "0" "9"))', resource_parts[i], flags = re.DOTALL)
                    if i == 5: # replace the last part of the ARN if a regex has not been defined for the resource resource_type yet.
                        resource_parts[i] = re.sub('\$\{.+\}', '(re.* (re.union (re.range "A" "Z") (re.range "a" "z") (re.range "0" "9") (str.to.re "_") (str.to.re "+") (str.to.re "=") (str.to.re ",") (str.to.re ".") (str.to.re "@") (str.to.re "\") (str.to.re "-")))', resource_parts[i], flags = re.DOTALL)
                
                smt += ' (str.in.re resource'
                smt += ' (re.++'
                smt += ' (str.to.re "arn:aws:")'
                smt += ' (str.to.re "' + namespace + ':")'
                
                if not resource_parts[3] == '':
                    smt += ' ' + resource_parts[3]
                
                smt += ' (str.to.re ":")'
                
                if not resource_parts[4] == '':
                    smt += ' ' + resource_parts[4]
                
                smt += ' (str.to.re ":")'
                
                if (not resource_parts[5] == '') and (not resource_parts[5] == '\*'):
                    if flag == 1:
                        smt += ' (re.++ ' + resource_parts[5] + ')'
                    else:
                        smt += ' ' + resource_parts[5]
                else:
                    smt += ' (str.to.re "*")'
                
                smt += '))' 
            
            # add assertions on (action, resource) pairings
            if resource_type in actions and len(actions[resource_type]) > 0:
                smt += ' (or'
                
                for action in actions[resource_type]:
                    smt += ' (= action "{}:{}")'.format(namespace, action)
                
                smt += ')'
            smt += ')'
        smt += ')'

    smt_json[namespace] = smt
    
# dump constraints to file
file = open('constraints_z3.json', 'w')
file.write(json.dumps(smt_json, indent=4))
file.close()