#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 23.py
# 2016/10/11(火)
# walkingmask

import json
# load json data from file
articles = []
for jsons in open("jawiki-country.json", 'r'):
  articles.append(json.loads(jsons))
# U.K.
for country in articles:
  if country['title'] == 'イギリス':
    break

def sectionLevel(mojiretsu):
  level = 1
  for i in range(2,len(mojiretsu)):
    if mojiretsu[i] != '=':
      break
    else:
      level += 1
  return level

import re

for line in country['text'].split("\n"):
  match = re.match(r"(=.*=)", line)
  if match != None:
    print(sectionLevel(match.group(1)), match.group(1))
