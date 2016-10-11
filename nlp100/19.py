#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 19.py
# 2016/10/11(火)
# walkingmask

# cut -f1 hightemp.txt | sort | uniq -c | sort -k1 -n -r

print('Hello, World!')

sorteds = []

for line in open('hightemp.txt', 'r'):
  sorteds.append(line.split("\t")[0])

from collections import Counter
uniqs = Counter(sorteds)

print(uniqs)
