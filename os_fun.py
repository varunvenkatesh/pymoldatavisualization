#!/usr/bin/python
import os

def intro():
    print "This section is going to be all about using the OS import"
    
def loopProps():
    print "Printing OS environment variables:"
    
    for key in os.environ.keys():
        print "%30s %s \n" % (key,os.environ[key])    

def main():
    intro()
    loopProps()