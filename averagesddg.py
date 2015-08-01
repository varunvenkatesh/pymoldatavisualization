#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import math
import os
import random
import re
## Method to get rid of white space in the datafile
TARGETFILE = "/Users/varunvenkatesh/Downloads/example"
LIMIT = 10
numbers = []

fstream    = open(TARGETFILE+".rtf", "r")

###
# Temp file for caching injected values:
###
#fstreamtmp = open(TARGETFILE+".rtf.tmp", "w")


i = 0
for line in fstream:
    line = re.sub(r' +', r' ', line.rstrip())    
    columns = line.rstrip().split(' ')
    ###
    # 105          102       925.0574
    # "105 102 925.0574"
    # columns[0] = 105
    # columns[1] = 102
    # columns[2] = 925.0754
    #
    ###
    print line
    #numbers[i] = 
    #print columns[1]
    i += 1
    # Build our string:
    #tuple = ""
    #for word in columns:
    #    tuple += word + " "
