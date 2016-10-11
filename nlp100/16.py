#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 16.py
# 2016/10/11(火)
# walkingmask

# check
# split -num filename

import sys

if len(sys.argv) != 3:
  print("Usage: ./15.py num filename")
  sys.exit()

splitNum = int(sys.argv[1])
fileName = sys.argv[2]
lineNum = 0
fileNum = 0

f = open('split'+str(fileNum), 'w')
for line in open(fileName, 'r'):
  if lineNum%splitNum == 0:
    if lineNum == 0:
      pass
    else:
      f.close()
      fileNum += 1
      f = open('split'+str(fileNum), 'w')
  f.write(line)
  lineNum += 1
else:
  try:
    f.close()
  except:
    pass
