#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser(description="removes each specified file. By default, it does not remove directories")
parser.add_argument("-r", '--recursive', help="remove directories and their contents recursively", action="store_true")
parser.add_argument("file", help="File or dir", nargs="+")
args = parser.parse_args()

if args.recursive is False:
    for file in args.file:
        os.remove(file)

if args.recursive is True:
    for dir in args.file:
        os.rmdir(dir)
