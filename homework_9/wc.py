#!/usr/bin/env python3

import sys


def l(f):
    """-l number of lines"""
    i = 0
    for line in f:
        i += 1
    return i


def w(f):
    """-w number of words"""
    i = 0
    for line in f:
        i += len(line.split())
    return i


def c(f):
    """-c count of bytes"""
    i = 0
    for line in f:
        i += bytes(line, 'utf-8')
    return i


settings = list(sys.argv[1:-1])
file = sys.argv[-1]
res = []

with open(file, 'r') as f:
    if not settings:
        settings = ['-l', '-w', '-c']

    if '-l' in settings:
        res.append(l(f))

    if '-w' in settings:
        res.append(w(f))

    if '-c' in settings:
        res.append(c(f))

print(res, file)

input()
