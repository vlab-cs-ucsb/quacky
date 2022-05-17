# builds GCP action encoding (offline)

import json

actions_json = json.loads(open('actions.json', 'r').read())

encoding_json = {}
encoding_json['_all'] = {}

n = 0
D = 3 # number of digits in encoding

# iterate over resource types
for resource_type in actions_json.keys():
    lo = n
    encoding_json[resource_type] = {}
    
    # iterate over actions
    actions = actions_json[resource_type]
    for action in actions:
        encoding_json[resource_type][action] = str(n).zfill(D)

        # add to 1:m mapping of actions to ids
        encoding_json['_all'][action] = str(n).zfill(D)
        
        n += 1

    hi = n - 1

    # store lo and hi bounds for each provider
    encoding_json[resource_type]['_lo'] = str(lo).zfill(D)
    encoding_json[resource_type]['_hi'] = str(hi).zfill(D)

# store global lo and hi bounds
encoding_json['_lo'] = str(0).zfill(D)
encoding_json['_hi'] = str(n - 1).zfill(D)

# dump encoding to file
file = open('encoding_actions.json', 'w')
file.write(json.dumps(encoding_json, indent=4))
file.close()