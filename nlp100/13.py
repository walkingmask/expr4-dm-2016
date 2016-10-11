#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 13.py
# 2016/10/11(火)
# walkingmask

# check
# paste col1.txt col2.txt 

col1f = open('col1.txt', 'r')
col2f = open('col2.txt', 'r')
copy = open('hightemp_copy.txt', 'w')

for col1, col2 in zip(col1f, col2f):
  copy.write(col1.rstrip()+"\t"+col2)

col1f.close()
col2f.close()
copy.close()
