#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 14.py
# 2016/10/11(火)
# walkingmask

# check
# head -n num filename

import sys

if len(sys.argv) != 3:
  print("Usage: ./14.py num filename")
  sys.exit()

lineNum = int(sys.argv[1])
fileName = sys.argv[2]

for line in open(fileName, 'r'):
  if lineNum <= 0:
    sys.exit()
  print(line, end="")
  lineNum -= 1
