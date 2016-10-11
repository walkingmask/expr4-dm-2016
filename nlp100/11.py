#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 11.py
# 2016/10/11(火)
# walkingmask

# check
# cat hightemp.txt | tr '\t' ' ' 

for line in open('hightemp.txt', 'r'):
  print(line.replace("\t"," "), end="")
