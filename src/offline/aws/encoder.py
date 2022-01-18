# builds AWS action encoding (offline)

import json

actions_json = json.loads(open('actions.json', 'r').read())

encoding_json = {}
encoding_json['_all'] = {}

n = 0

# iterate over namespaces
for namespace in actions_json.keys():
    lo = n
    encoding_json[namespace] = {}

    # iterate over resource types
    resource_types = actions_json[namespace]
    for resource_type in resource_types.keys():
        encoding_json[namespace][resource_type] = {}
        
        # iterate over actions
        actions = resource_types[resource_type]
        for action in actions:
            encoding_json[namespace][resource_type][action] = str(n).zfill(5)

            # add to 1:m mapping of actions to ids
            if namespace + ':' + action not in encoding_json['_all']:
                encoding_json['_all'][namespace + ':' + action] = [str(n).zfill(5)]
            else:
                encoding_json['_all'][namespace + ':' + action].append(str(n).zfill(5))
            n += 1

    hi = n - 1

    # store lo and hi bounds for each namespace
    encoding_json[namespace]['_lo'] = str(lo).zfill(5)
    encoding_json[namespace]['_hi'] = str(hi).zfill(5)

    # store global lo and hi bounds
    encoding_json['_lo'] = str(0).zfill(5)
    encoding_json['_hi'] = str(n - 1).zfill(5)

# dump encoding to file
file = open('encoding.json', 'w')
file.write(json.dumps(encoding_json, indent=4))
file.close()