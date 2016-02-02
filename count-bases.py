#! /usr/bin/env python
# This script shows how we can open and read files in python.

from sys import argv, exit

try:
    # Try to open the file:
    f = open(argv[1], "r")
except:
    #If there is an error, give up:
    print("ERROR: Failed to open input file")
    exit(1)

# Set up the data:
bases = ['A', 'C', 'G', 'T', 'N']
counts = {}
for base in bases:
    counts[base] = 0

# Iterate through the file:
line_n = 0
for line in f.readlines():
    line = line.strip()
    line_n = line_n + 1
    mod = line_n % 4
    if mod == 2:
        for base in bases:
            counts[base] += line.count(base)

# Print out the data:
for base in bases:
    print('{}\t{}'.format(base, counts[base]))
