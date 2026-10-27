#!/usr/bin/env python

import sys


fname = 'x.csv'
with open(fname, 'r') as f:
    l = f.readline()
    while l != '':
        sys.stderr.write(l)
        l = f.readline()

