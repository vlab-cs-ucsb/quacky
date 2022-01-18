# scrapes GCP resource type and action mapping from GCP portal

from bs4 import BeautifulSoup
import json
import re

actions_json = {}
resource_types_map = {}

# process resource types
rt_regex = '\w+\.googleapis\.com/\w+'

with open('resource_types.xml', 'r') as f:
    xml = f.read()

resource_types = [rt.lower() for rt in re.findall(rt_regex, xml)]

with open('resource_types.json', 'w') as f:
    f.write(json.dumps(resource_types))

for rt in resource_types:
    prefix = rt.split('.')[0]
    suffix = rt.split('/')[-1]

    resource_types_map[(prefix, suffix)] = rt

# parse HTML
html = open('permissions.html', 'r').read()
soup = BeautifulSoup(html, 'html.parser')

# actions are in <code> blocks
code_elements = soup.find_all('code', {'class': None})

# extract action foo.bar.baz
for e in code_elements:
    action = e.text.lower()
    prefix, suffix = action.split('.')[:2]

    # handle plurals
    if suffix.endswith('s'):
        suffix = suffix[:-1]
    
    if (prefix, suffix) in resource_types_map:
        rt = resource_types_map[(prefix, suffix)]

        if rt in actions_json:
            actions_json[rt].append(action)
        else:
            actions_json[rt] = [action]

file = open('actions.json', 'w')
file.write(json.dumps(actions_json, indent=4))
file.close()