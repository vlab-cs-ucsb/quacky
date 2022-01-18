# scrapes Azure resource type and action mapping from csv from Azure portal

import csv
import json

# open csv exported from Azure portal
csv_file = open('permissions.csv', encoding='utf-8')
csv_reader = csv.DictReader(csv_file)

actions_json = {}
data_actions_json = {}

for row in csv_reader:
    data_action = row['Data Action']
    
    if data_action == 'FALSE':
        # get resource provider
        resource_provider = row['Resource Provider'].lower()
        if resource_provider not in actions_json:
            actions_json[resource_provider] = {}

        # get resource type
        resource_type = row['Resource Type'].lower()
        if resource_type not in actions_json[resource_provider]:
            actions_json[resource_provider][resource_type] = []

        # get action name
        action_name = row['Operation Name'].lower()
        action_name = action_name.replace(resource_provider + '/', '')
        if resource_type != '':
            action_name = action_name.replace(resource_type + '/', '')
        
        if action_name not in actions_json[resource_provider][resource_type]:
            actions_json[resource_provider][resource_type].append(action_name)
    
    else:
        # get resource provider
        resource_provider = row['Resource Provider'].lower()
        if resource_provider not in data_actions_json:
            data_actions_json[resource_provider] = {}

        # get resource type
        resource_type = row['Resource Type'].lower()
        if resource_type not in data_actions_json[resource_provider]:
            data_actions_json[resource_provider][resource_type] = []

        # get action name
        action_name = row['Operation Name'].lower()
        action_name = action_name.replace(resource_provider + '/', '')
        if resource_type != '':
            action_name = action_name.replace(resource_type + '/', '')
        
        if action_name not in data_actions_json[resource_provider][resource_type]:
            data_actions_json[resource_provider][resource_type].append(action_name)

# dump constraints to files
file = open('actions.json', 'w')
file.write(json.dumps(actions_json, indent=4))
file.close()

file = open('data_actions.json', 'w')
file.write(json.dumps(data_actions_json, indent=4))
file.close()