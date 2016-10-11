#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 06.py
# 2016/10/11(火)
# walkingmask

# return list
def charNgram(mojiretsu,n):
  data = [mojiretsu[i:i+n] for i in range(0,len(mojiretsu))]
  return data

set1 = set(charNgram("paraparaparadise",2))
set2 = set(charNgram("paragraph",2))

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print("se" in set1.union(set2))
