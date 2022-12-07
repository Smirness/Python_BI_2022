#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="command for quickly accessing the last few lines of a given text file")
parser.add_argument("-n", help="number of lines", default=['10'], type=str, nargs=1)
parser.add_argument("file", help="File", nargs="+")
args = parser.parse_args()

with open(args.file[0], 'r') as f:
    end = len(f.readlines())
    start = end - int(args.n[0])

with open(args.file[0], 'r') as f:
    lines = f.readlines()

for line in lines[start:end]:
    print(line, end='')
