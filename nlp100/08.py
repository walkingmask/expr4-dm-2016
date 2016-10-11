#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 08.py
# 2016/10/11(火)
# walkingmask

def cipher(mojiretsu):
  lcl = "abcdefghijklmnopqrstuvwxyz"
  mojiretsu_list = list(mojiretsu)
  for i in range(0, len(mojiretsu_list)):
    if mojiretsu_list[i] in lcl:
      mojiretsu_list[i] = chr(219 - ord(mojiretsu_list[i]))
  return "".join(mojiretsu_list)

print(cipher("I am an NLPer"))
print(cipher(cipher("I am an NLPer")))