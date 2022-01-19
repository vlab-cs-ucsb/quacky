# Converts Markdown results to CSV

import re
import sys

symbols = ['[', ']', '..', '-']

mdfile = open(sys.argv[1], 'r')

mdtable = [line for line in mdfile.readlines() if line[0] == '|']
mdheader = mdtable[0]
mdbody = mdtable[2:]

csv = ''

csvheader = mdheader.replace('|', ',')[1:-2] + '\n'
csv += csvheader

for mdrow in mdbody:
    csvrow = mdrow.replace('|', ',')[1:-2] + '\n'
    csvrow = re.sub('\(\.\.[^,()]*\.json\)', '', csvrow)

    for symbol in symbols:
        csvrow = csvrow.replace(symbol, '')
    
    csv += csvrow

csvfile = open(sys.argv[1].replace('.md', '') + '.csv', 'w')
csvfile.write(csv)
csvfile.close()
