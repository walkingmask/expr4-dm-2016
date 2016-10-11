#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 12.py
# 2016/10/11(火)
# walkingmask

# check
# cut -f1 hightemp.txt
# cut -f2 hightemp.txt

col1f = open('col1.txt', 'w')
col2f = open('col2.txt', 'w')

for line in open('hightemp.txt', 'r'):
  raw = line.rstrip().replace("\t"," ").split(" ")
  col1f.write(raw[0]+"\n")
  col2f.write(raw[1]+"\n")

col1f.close()
col2f.close()
