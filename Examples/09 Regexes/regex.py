#!/usr/bin/python3

import re


fh = open('raven.txt')
for line in fh:
    if re.search('(Len|Neverm)ore', line):
        print(line, end='')


