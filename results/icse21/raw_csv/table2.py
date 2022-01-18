import csv
import math

datasets = ['ec2_action_resource', 'iam_action_resource', 's3_action_resource']

for dataset in datasets:
    reader = csv.reader(open('README_{}_nolog.csv'.format(dataset), 'r'))

    data = list(reader)[1:-1]

    for i in range(len(data)):
        for j in [4, 6, 7, 8, 11, 13, 14, 15]:
            if data[i][j] == '':
                data[i][j] == 0
            else:
                data[i][j] = int(data[i][j])

    policies = set([line[0] for line in data])

    for policy in policies:
        if policy == 'Policy 1':
            continue

        out = ''

        out += policy + ','

        for i in [4, 6, 7, 8]:
            try:
                total = sum([int(line[i]) for line in data if line[0] == policy and line[2] != 'UNSAT'])
                out += str(math.log2(total // len([int(line[i]) for line in data if line[0] == policy and line[2] != 'UNSAT']))) + ','
            except:
                out += ','

        for i in [11, 13, 14, 15]:
            try:
                total = sum([int(line[i]) for line in data if line[0] == policy and line[9] != 'UNSAT'])
                out += str(math.log2(total // len([int(line[i]) for line in data if line[0] == policy and line[9] != 'UNSAT']))) + ','
            except:
                out += ','
        
        for i in [4, 6, 7, 8]:
            try:
                total2 = sum([math.log2(int(line[i])) for line in data if line[0] == policy and line[2] != 'UNSAT'])
                out += str((total2 / len([int(line[i]) for line in data if line[0] == policy and line[2] != 'UNSAT']))) + ','
            except:
                out += ','

        for i in [11, 13, 14, 15]:
            try:
                total2 = sum([math.log2(int(line[i])) for line in data if line[0] == policy and line[9] != 'UNSAT'])
                out += str((total2 / len([int(line[i]) for line in data if line[0] == policy and line[9] != 'UNSAT']))) + ','
            except:
                out += ','

        out = out[:-1]

        print(out)
