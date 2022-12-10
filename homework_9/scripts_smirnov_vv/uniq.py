#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="Discard all but one of successive identical lines from INPUT (or standard input)")
parser.add_argument("file", help="File", nargs="+")
args = parser.parse_args()

res = []
with open(args.file[0]) as f:
    # prev_line = f.readline()
    prev_line = []
    for line in f:
        if line != prev_line:
            prev_line = line
            res.append(line)

for line in res:
    print(line, end='')
