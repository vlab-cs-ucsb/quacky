import csv
import math

datasets = ['ec2', 'iam', 's3']

for dataset in datasets:
    reader = csv.reader(open('{}.csv'.format(dataset), 'r'))

    data = list(reader)[1:]

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

        total = sum([float(line[3]) + float(line[10]) for line in data if line[0] == policy])
        total += sum([float(line[5]) for line in data if line[0] == policy and line[2] == 'SAT'])
        total += sum([float(line[12]) for line in data if line[0] == policy and line[9] == 'SAT'])
        out += str(total / (len([line for line in data if line[0] == policy]) * 1000)) + ','

        total = len([line for line in data if line[0] == policy and line[2] == 'SAT' and line[9] == 'UNSAT'])
        out += str(total) + ','
        total = len([line for line in data if line[0] == policy and line[2] == 'UNSAT' and line[9] == 'SAT'])
        out += str(total) + ','
        total = len([line for line in data if line[0] == policy and line[2] == 'UNSAT' and line[9] == 'UNSAT'])
        out += str(total) + ','
        total = len([line for line in data if line[0] == policy and line[2] == 'SAT' and line[9] == 'SAT'])
        out += str(total) + ','

        for i in [4]:
            try:
                total = sum([int(line[i]) for line in data if line[0] == policy and line[2] == 'SAT' and line[9] == 'UNSAT'])
                out += str(math.log2(total // len([line for line in data if line[0] == policy and line[2] == 'SAT' and line[9] == 'UNSAT']))) + ','
            except:
                out += ','
        
        for i in [4]:
            try:
                total2 = sum([math.log2(int(line[i])) for line in data if line[0] == policy and line[2] == 'SAT' and line[9] == 'UNSAT'])
                out += str((total2 / len([line for line in data if line[0] == policy and line[2] == 'SAT' and line[9] == 'UNSAT']))) + ','
            except:
                out += ','

        for i in [11]:
            try:
                total = sum([int(line[i]) for line in data if line[0] == policy and line[2] == 'UNSAT' and line[9] == 'SAT'])
                out += str(math.log2(total // len([line for line in data if line[0] == policy and line[2] == 'UNSAT' and line[9] == 'SAT']))) + ','
            except:
                out += ','

        for i in [11]:
            try:
                total2 = sum([math.log2(int(line[i])) for line in data if line[0] == policy and line[2] == 'UNSAT' and line[9] == 'SAT'])
                out += str((total2 / len([line for line in data if line[0] == policy and line[2] == 'UNSAT' and line[9] == 'SAT']))) + ','
            except:
                out += ','

        out = out[:-1]

        print(out)




    
            

    
    
