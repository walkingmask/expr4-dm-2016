#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 18.py
# 2016/10/11(火)
# walkingmask

# ref
# http://blog.livedoor.jp/yawamen/archives/51492355.html

# sort -k 3 hightemp.txt 

sorteds = {}
lineNum = 0

for line in open('hightemp.txt', 'r'):
  sorteds[line.rstrip()] = float(line.split("\t")[2])

for k, v in sorted(sorteds.items(), key=lambda x:x[1]):
  print(k)
