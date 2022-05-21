import csv
import math
import sys

csvfile = open(sys.argv[1], 'r')
reader = csv.reader(csvfile, delimiter=',')
next(reader)

perms = []
times = []

for row in reader:
    try:
        perms.append(int(row[3]))
    except:
        perms.append(0)

    try:
        times.append(float(row[2]) + float(row[4]))
    except:
        times.append(float(row[2]))

print(f'mean log perm: {math.log2(sum(perms) // len(perms))}')
print(f'mean time (ms): {sum(times) / len(times)}')

csvfile.close()