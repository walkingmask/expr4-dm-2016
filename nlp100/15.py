#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 15.py
# 2016/10/11(火)
# walkingmask

# check
# tail -n num filename

import sys

if len(sys.argv) != 3:
  print("Usage: ./15.py num filename")
  sys.exit()

lineNum = int(sys.argv[1])
fileName = sys.argv[2]
lines = sum(1 for line in open(fileName))

for line in open(fileName, 'r'):
  if lines <= lineNum:
    print(line, end="")
  lines -= 1
