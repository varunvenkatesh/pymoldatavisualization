#!/usr/bin/python

import sys

def intro():
    print "This section is going to be all about data structures"
    
def list():
    print "Let's have fun with lists:"
    alphabet = ['a','b','c','d','e','f','g',
         'h','i','j','k','l','m','n',
         'o','p','q','r','s','t','u',
         'v','w','x','y','z']
    print("First letter of the alphabet is {0}".format(alphabet[0]))    
    print("The English alphabet in lower case is:")
    print ' '.join(alphabet)
    print("The English alphabet in upper case is:")   
    for i in alphabet:
        print("{0}".format(i)),
         
    
def main():
    intro()
    list()
    
main()