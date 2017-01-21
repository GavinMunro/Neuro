#!/usr/bin/env python
#
# Title           :ReadEEG.py
# Author          :Gavin A.I. Munro
# Date            :14/1/17
# Version         :0.1

import csv

# This module is to read in a file 8 columns of hex numbers and convert them 
# to decimal for plotting in some sort of time series graph.

'''
open returns a file which can be iterated over. When you iterate over a file, you get the lines from that file. 
tuple can take an iterator and instantiate a tuple instance for you from the iterator that you give it. 
lines is a tuple created from the lines of the file
Noctis Skytower  StackOverflow  Jan 5 '14 at 21:58
'''
# So, if we might need to keep the list/tuple around we could use:
# lines = tuple(open(filename, 'r'))
# or as a list:
# lines = list(open(infilepath, 'r'))

infilepath = "/home/gaz/code/Braintrain/test1.dat"
# ToDo: Might later need proper os.path join etc.
delim = ' '


# Test file reading and writing is occurring
with open(infilepath, 'r') as f:
    lines = f.read().splitlines()  # Removes `\n` at the end of each line
lines = lines[:200]   # Stop after 200 lines for now just to test output
for line in lines:
    print(line)


# Now to try using generators with "yield"
def readAllRows(filepath, delimiter):
    with open(filepath, 'r') as f:
        for line in f:
            yield list(line.split(delimiter))

'''
def readLines():
    with open(infilepath, 'r') as f:
        content = f.read().splitlines()  # Removes `\n` at the end of each line
        for line in content:
            print(line)
            l = list(line.split(delim))
            print(l)
            print([int(x, 16) for x in l])
            #(int(x) for x in r)
            #row = [hex.strip() for hex in content]
'''

# Let's create a file called 'decout.txt' to write the output to
outfilepath = "/home/gaz/code/Braintrain/decout.txt"
with open(outfilepath, 'w+') as f:
    writer = csv.writer(f)
    #dec8 = [int(hex, 16) for hex in row]
    for row in readAllRows(infilepath, delim):
        dec8 = [int(hex, 16) for hex in row]
        writer.writerow(dec8)
# The file is now closed by "with"



