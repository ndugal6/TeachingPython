#!/usr/bin/python2.7

import re


fh = open('raven.txt')
for line in fh:
    if re.search('(Len|Neverm)ore', line):
        print(line, end='')


