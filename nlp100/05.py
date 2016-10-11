#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 05.py
# 2016/10/05(水)
# walkingmask
# what is n-gram
# http://d.hatena.ne.jp/jetbead/20110904/1315147133

from collections import Counter

def charNgram(mojiretsu,n):
  data = [mojiretsu[i:i+n] for i in range(0,len(mojiretsu))]
  counter = Counter(data)
  return counter

def wordNgram(mojiretsu,n):
  data = [' '.join(mojiretsu.split(" ")[i:i+n]) for i in range(0,len(mojiretsu.split(" "))-n+1)]
  counter = Counter(data)
  return counter

print(wordNgram("I am an NLPer",2))
print(charNgram("I am an NLPer",2))