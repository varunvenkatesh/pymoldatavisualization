#!/usr/bin/python
import random

number = 8822

for i in xrange(number):
    print random.randint(-3, 3),
    # TODO: figure out how to get rid of last comma in file
    print ",",
    

###
# STEP 1 -
# TODO: Instead of printing the contents to a file, just put them in a list or other data structure:
###   


# Open a file
fo = open("foo.txt", "wb")
for i in xrange(number):
    # TODO: figure out how to get rid of last comma in file     
    fo.write(str(random.randint(-3, 3)) + ",")
# Close opend file
fo.close()

###
# STEP 2 -
# Open pdb file for reading and writing ("wb")
### 

###
# STEP 3 -
# Be able to read numbers in the list and replace the values in the pdb file with the list values
# Go into the pdb file and replace the second to last column using one to one mapping with the values from the list 
###