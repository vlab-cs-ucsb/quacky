# builds Azure action encoding (offline)

import json

actions_json = json.loads(open('actions.json', 'r').read())
data_actions_json = json.loads(open('data_actions.json', 'r').read())

encoding_json = {}
encoding_json['_all'] = {}

n = 0
D = 5 # number of digits in encoding

# iterate over providers
for provider in actions_json.keys():
    lo = n
    encoding_json[provider] = {}

    # iterate over resource types
    resource_types = actions_json[provider]
    for resource_type in resource_types.keys():
        encoding_json[provider][resource_type] = {}
        
        # iterate over actions
        actions = resource_types[resource_type]
        for action in actions:
            encoding_json[provider][resource_type][action] = str(n).zfill(D)

            # add to 1:m mapping of actions to ids
            if resource_type == '':
                encoding_json['_all']['/'.join([provider, action])] = str(n).zfill(D)
            else:
                encoding_json['_all']['/'.join([provider, resource_type, action])] = str(n).zfill(D)
            
            n += 1

    hi = n - 1

    # store lo and hi bounds for each provider
    encoding_json[provider]['_lo'] = str(lo).zfill(D)
    encoding_json[provider]['_hi'] = str(hi).zfill(D)

# store global lo and hi bounds
encoding_json['_lo'] = str(0).zfill(D)
encoding_json['_hi'] = str(n - 1).zfill(D)

# dump encoding to file
file = open('encoding_actions.json', 'w')
file.write(json.dumps(encoding_json, indent=4))
file.close()

encoding_json = {}
encoding_json['_all'] = {}

for provider in data_actions_json.keys():
    lo = n
    encoding_json[provider] = {}

    resource_types = data_actions_json[provider]
    for resource_type in resource_types.keys():
        encoding_json[provider][resource_type] = {}
        
        data_actions = resource_types[resource_type]
        for action in data_actions:
            encoding_json[provider][resource_type][action] = str(n).zfill(D)

            # add to 1:m mapping of actions to ids
            if resource_type == '':
                encoding_json['_all']['/'.join([provider, action])] = str(n).zfill(D)
            else:
                encoding_json['_all']['/'.join([provider, resource_type, action])] = str(n).zfill(D)
            
            n += 1

    hi = n - 1

    # store lo and hi bounds for each provider
    encoding_json[provider]['_lo'] = str(lo).zfill(D)
    encoding_json[provider]['_hi'] = str(hi).zfill(D)

# store global lo and hi bounds
encoding_json['_lo'] = str(0).zfill(D)
encoding_json['_hi'] = str(n - 1).zfill(D)

# dump encoding to file
file = open('encoding_data_actions.json', 'w')
file.write(json.dumps(encoding_json, indent=4))
file.close()
