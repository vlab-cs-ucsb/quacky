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

        out = policy + ','

        count = len([line for line in data if line[0] == policy])
        out += str(count) + ','
        
        time = sum([float(line[3]) / 1000 for line in data if line[0] == policy]) # solve 1
        time += sum([float(line[5]) / 1000 for line in data if line[0] == policy and line[2] == 'SAT']) # count 1
        time += sum([float(line[10]) / 1000 for line in data if line[0] == policy]) # solve 2
        time += sum([float(line[12]) / 1000 for line in data if line[0] == policy and line[9] == 'SAT']) # count 2

        out += str(time / len([line for line in data if line[0] == policy])) + ','

        mutant_less = len([line for line in data if line[0] == policy and line[2] == 'SAT' and line[9] == 'UNSAT'])
        out += '{} ({}%),'.format(mutant_less, (mutant_less / count) * 100)        
        mutant_more = len([line for line in data if line[0] == policy and line[2] == 'UNSAT' and line[9] == 'SAT'])
        out += '{} ({}%),'.format(mutant_more, (mutant_more / count) * 100)
        mutant_eq = len([line for line in data if line[0] == policy and line[2] == 'UNSAT' and line[9] == 'UNSAT'])
        out += '{} ({}%),'.format(mutant_eq, (mutant_eq / count) * 100)
        mutant_incomp = len([line for line in data if line[0] == policy and line[2] == 'SAT' and line[9] == 'SAT'])
        out += '{} ({}%),'.format(mutant_incomp, (mutant_incomp / count) * 100)

        # log arithmetic mean of tuple count for less permissive mutants
        try:
            total = sum([int(line[4]) for line in data if line[0] == policy and line[2] == 'SAT' and line[9] == 'UNSAT'])
            out += str(math.log2(total // mutant_less)) + ','
        except:
            out += ','

        # log geometric mean of tuple count for less permissive mutants
        try:
            total = sum([math.log2(int(line[4])) for line in data if line[0] == policy and line[2] == 'SAT' and line[9] == 'UNSAT'])
            out += str((total / mutant_less)) + ','
        except:
            out += ','

        # log arithmetic mean of tuple count for more permissive mutants
        try:
            total = sum([int(line[11]) for line in data if line[0] == policy and line[2] == 'UNSAT' and line[9] == 'SAT'])
            out += str(math.log2(total // mutant_more)) + ','
        except:
            out += ','

         # log geometric mean of tuple count for less permissive mutants
        try:
            total = sum([math.log2(int(line[11])) for line in data if line[0] == policy and line[2] == 'UNSAT' and line[9] == 'SAT'])
            out += str((total / mutant_more)) + ','
        except:
            out += ','

        out = out[:-1]

        print(out)




    
            

    
    
