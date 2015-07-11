#!/usr/bin/python
import os
import random
import re
 
# Constants and global members:
TARGETFILE = "TtLSU"
LIMIT = 8822
numbers = [];

###
# Generate a bunch of test data values and insert into an array 
# (list). Don't worry about putting it into a file. Make sure
# to cast to a string as this will make the injection phase
# trivial (easy).
###
for i in xrange(LIMIT):
    numbers.insert(i, str(random.randint(-3, 3)))

###
# Main pdb data file:
###
fstream    = open(TARGETFILE+".pdb", "r")

###
# Temp file for caching injected values:
###
fstreamtmp = open(TARGETFILE+".pdb.tmp", "w")

###
# Convert PDB into a space delimeted format then split
# on each space. Next inject each number from our list into 
# each tuple (row) for the 10th column.
###
i = 0
for line in fstream:
    line = re.sub(r' +', r' ', line.rstrip())    
    columns = line.rstrip().split(' ');
    columns[9] = numbers[i]
    i += 1
    # Build our string:
    tuple = ""
    for word in columns:
        tuple += word + " "

    # Uncomment line below to print each tuple (row) to STDOUT for testing.
    # print tuple.rstrip()

    # Dump each tuple (row) into the tmp file.
    # The split removes the extra white space.
    fstreamtmp.write(str(tuple.rstrip()) + "\n")

fstream.close()
fstreamtmp.close()

# Superimpose (write over) contents of original pdb with pdb.tmp file:
os.rename(TARGETFILE+".pdb.tmp", TARGETFILE+".pdb")
