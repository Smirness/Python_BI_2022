#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="It is used to find out number of lines, word count, byte specified in the files")
parser.add_argument("-l", help="number of lines", action="store_true")
parser.add_argument("-w", help="number of words", action="store_true")
parser.add_argument("-c", help="count of bytes", action="store_true")
parser.add_argument("file", help="File", nargs="+")
args = parser.parse_args()


def l(f):
    """-l number of lines"""
    with open(f, 'r') as f:
        i = 0
        for line in f:
            i += 1
    return i


def w(f):
    """-w number of words"""
    with open(f, 'r') as f:
        i = 0
        for line in f:
            i += len(line.split())
    return i


def c(f):
    """-c count of bytes"""
    with open(f, 'rb') as f:
        return len(f.read())


file = str(args.file[0])
res = []

if args.l is False and args.w is False and args.c is False:
    args.l = True
    args.w = True
    args.c = True

if args.l is True:
    res.append(l(file))

if args.w is True:
    res.append(w(file))

if args.c is True:
    res.append(c(file))

print(*res, file)
