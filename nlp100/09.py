#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 09.py
# 2016/10/11(火)
# walkingmask

import random

def typoglycemia(bun):
  tangos = bun.split(" ")
  for tango in tangos:
    if len(tango) <= 4:
      print(tango, end=' ')
    else:
      print(tango[0]+tangoShuffle(tango[1:-1])+tango[-1], end=' ')

def tangoShuffle(tango):
  return "".join(random.sample(tango,len(tango)))

print(typoglycemia("I could not believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))
