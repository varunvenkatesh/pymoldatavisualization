#!/usr/bin/python
import re
import random
 
number = 8822
# Open a file
fo = open("ddginput.txt", "wb")
for i in xrange(number):
    # TODO: figure out how to get rid of last comma in file     
    fo.write(str(random.randint(-3, 3)) + ",")
# Close opend file
fo.close()

# Read in the pdb data file:
#fstream = open("tester.txt", "r")
fstream = open("TtLSU.pdb", "r")
for line in fstream:
    print line.strip()
        #line = re.sub(r' +', r' ', line.rstrip())    

## with open('test1.txt', 'w') as outf:
##    for line in inf:
##        line = line.strip()
##        if line:
##            try:
##                outf.write(int(line, 16))
##                outf.write('\n')
##            except ValueError:
##                print("Could not parse '{0}'".format(line))
