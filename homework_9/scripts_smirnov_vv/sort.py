#!/usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser(description="SORT command is used to sort a file, arranging the records in a particular order.")
parser.add_argument("file", help="Input file", type=str)
args = parser.parse_args()

res = []

if not args.file:
    for line in sys.stdin:
        res.append(line)

else:
    with open(args.file, 'r') as f:
        for line in f:
            res.append(line)

res.sort()

for line in res:
    print(line, end='')
