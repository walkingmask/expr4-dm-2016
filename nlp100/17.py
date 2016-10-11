#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 17.py
# 2016/10/11(火)
# walkingmask

# cut -f1 hightemp.txt | sort | uniq

sorteds = []

for line in open('hightemp.txt', 'r'):
  sorteds.append(line.split("\t")[0])

uniqs = set(sorteds)

print(uniqs)
