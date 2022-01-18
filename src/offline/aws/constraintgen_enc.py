# builds AWS resource type constraints using action encoding (offline)

import json
import re

# action encodings and corresponding resource types
actions_json = json.loads(open('actions.json', 'r').read())
encoding_json = json.loads(open('encoding.json', 'r').read())
resources_json = json.loads(open('resources.json', 'r').read())

# custom regex for ARNs and resource types
arn_regex = json.loads(open('arn_regex.json', 'r').read())
resource_regex = json.loads(open('resource_regex.json', 'r').read())

smt_json = {}

# iterate through all services
for namespace in actions_json.keys():
    encoding_json[namespace].pop('_lo')
    encoding_json[namespace].pop('_hi')
    
    resource_types = resources_json[namespace]

    smt = ''
    
    if len(resource_types) > 0:
        smt += '(or'
        
        for resource_type in encoding_json[namespace]:
            smt += ' (and'
            
            # if no resource type specified, use a generic ARN format for that resource type
            if resource_type == '':
                # check if there is a generic ARN in arg_regex.json
                if namespace in arn_regex:
                    resource = arn_regex[namespace]
                    
                    # substitute in regex representations of ${...}
                    resource = resource.replace('${Partition}', 'aws')
                    resource = resource.replace('${Region}', '(us(-gov)?|ap|ca|cn|eu|sa)-(central|(north|south)?(east|west)?)-[0-9][a-z]?')
                    resource = resource.replace('${Account}', '[0-9]{12,12}')
                    
                    smt += ' (in resource /' + resource + '/)' 
                
                # if no generic ARN in arg_regex.json, use the regex below
                else:
                    smt += ' (in resource /(arn:aws:' + namespace + ':((us(-gov)?|ap|ca|cn|eu|sa)-(central|(north|south)?(east|west)?)-[0-9][a-z]?)?:([0-9]{12})?:)?\*/)'
            
            # if resource type specified
            else:
                resource = resource_types[resource_type].replace('/', '\/')

                # substitute in regex representations of ${...}
                if namespace in resource_regex:
                    for obj, reg_expr in resource_regex[namespace].items():
                        resource = resource.replace('${' + obj + '}', reg_expr)
                
                resource = resource.replace('${Partition}', 'aws')
                resource = resource.replace('${Region}', '(us(-gov)?|ap|ca|cn|eu|sa)-(central|(north|south)?(east|west)?)-[0-9][a-z]?')
                resource = resource.replace('${Account}', '[0-9]{12,12}')
                
                # replace the last part of the ARN if a regex has not been defined for the resource type yet.
                resource = re.sub('\$\{.+\}', '[A-Za-z0-9_+=,.@\-]*', resource, flags = re.DOTALL)
                smt += ' (in resource /' + resource + '/)'
            
            # add assertions on (encoding, resource) pairings
            if resource_type in encoding_json[namespace] and len(encoding_json[namespace][resource_type]) > 0:
                lo = min(encoding_json[namespace][resource_type].values())
                hi = max(encoding_json[namespace][resource_type].values()) 
                
                if lo == hi:
                    smt += ' (= action "{}")'.format(lo)
                else:
                    smt += ' (and (>= action "{}") (<= action "{}"))'.format(lo, hi)

            smt += ')'
        smt += ')'

    smt_json[namespace] = smt

# dump constraints to file
file = open('constraints_enc.json', 'w')
file.write(json.dumps(smt_json, indent=4))
file.close()