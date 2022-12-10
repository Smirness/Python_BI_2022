#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser(description="it creates each directory specifed on the command line in the order given")
parser.add_argument("-p", '--parents', help="no error if existing, make parent directories as needed", action="store_true")
parser.add_argument("file", help="File", nargs="+")
args = parser.parse_args()

if args.parents is False:
    os.mkdir(args.file[0])

if args.parents is True:
    os.makedirs(args.file[0])
