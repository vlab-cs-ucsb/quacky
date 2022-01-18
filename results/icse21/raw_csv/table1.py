import csv
import math
import numpy as np

datasets = ['ec2', 'iam', 's3', 'ec2_action_resource', 'iam_action_resource', 's3_action_resource']

for dataset in datasets:
    reader = csv.reader(open('README_{}_single_nolog.csv'.format(dataset), 'r'))

    data = list(reader)[1:]

    out = ''

    total = sum([float(line[2]) + float(line[4]) for line in data if line[1] == 'SAT'] + [float(line[2]) for line in data if line[1] == 'UNSAT'])
    out += str(total / len([line for line in data])) + ','

    total = sum([int(line[3]) for line in data if line[1] != 'UNSAT'])
    out += str(math.log2(total // len([int(line[3]) for line in data if line[1] != 'UNSAT']))) + ','

    total = sum([int(line[5]) for line in data if line[1] != 'UNSAT'])
    out += str(math.log2(total // len([int(line[5]) for line in data if line[1] != 'UNSAT']))) + ','

    total = sum([int(line[6]) for line in data if line[1] != 'UNSAT'])
    out += str(math.log2(total // len([int(line[6]) for line in data if line[1] != 'UNSAT']))) + ','

    total = sum([int(line[7]) for line in data if line[1] != 'UNSAT'])
    out += str(math.log2(total // len([int(line[7]) for line in data if line[1] != 'UNSAT']))) + ','

    total = sum([math.log2(int(line[3])) for line in data if line[1] != 'UNSAT'])
    out += str((total / len([int(line[3]) for line in data if line[1] != 'UNSAT']))) + ','

    total = sum([math.log2(int(line[5])) for line in data if line[1] != 'UNSAT'])
    out += str((total / len([int(line[5]) for line in data if line[1] != 'UNSAT']))) + ','

    total = sum([math.log2(int(line[6])) for line in data if line[1] != 'UNSAT'])
    out += str((total / len([int(line[6]) for line in data if line[1] != 'UNSAT']))) + ','

    total = sum([math.log2(int(line[7])) for line in data if line[1] != 'UNSAT'])
    out += str((total / len([int(line[7]) for line in data if line[1] != 'UNSAT'])))

    print(out)
