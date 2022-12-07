#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser(description="List information about the FILEs (the current directory by default")
parser.add_argument("-a", '--all', help="do not ignore entries starting with", action="store_true")
parser.add_argument("file", help="File or path", default='./', nargs='?')
args = parser.parse_args()

res = []

if args.all is True:
    res = os.listdir(args.file)

if args.all is False:
    for d in os.listdir(args.file):
        if not d.startswith('.'):
            res.append(d)

print(*res)