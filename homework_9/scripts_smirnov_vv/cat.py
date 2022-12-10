#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser(description=" reads one or more files and prints their contents to standard output")
parser.add_argument("file", help="File", nargs="+")
args = parser.parse_args()

# get path, file, type file from input file
file = args.file[0]                         # for command 'cat.py *.txt'
path = os.path.dirname(args.file[0])
file = os.path.basename(args.file[0])       # for command with 'cat.py ./homework_9/test_sort.txt'
type_file = file.split('.')[-1]
abspath_to_f = os.path.abspath(file)
abspath = os.path.dirname(abspath_to_f)

# print(file)

# print all files. If command 'cat.py *'
if '*' in file and '*' in type_file:
    for file in os.listdir(abspath):
        with open(file, 'r') as f:
            for line in f:
                print(line, end='')

# print all files with specific filetype. If command 'cat.py *.txt'
elif '*' in file:
    for file in os.listdir(abspath):
        if file.endswith('.%s' %type_file):
            with open(file, 'r') as f:
                for line in f:
                    print(line, end='')

# print files with specific. If command 'cat.py test_sort.txt'
elif '*' not in file:
    with open(file,'r') as f:
        for line in f:
            print(line, end='')
