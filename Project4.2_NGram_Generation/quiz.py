#!/usr/bin/python

import os
import sys

dir = sys.argv[1]

linecount = 0
for i in os.listdir(dir):
  if i.startswith('part'):
    file = os.path.join(dir, i)
    fin = open(file, 'r')
    for line in fin:
      linecount += 1
      data = line.split('\t')
      if (data[0] == 'early in the morning'):
          print line
print 'Total lines:', linecount

