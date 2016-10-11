#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 22.py
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

import re

for line in country['text'].split("\n"):
  match = re.search(r"Category:(.*)]]", line)
  if match != None:
    if '|' in match.group(1):
      items = match.group(1).split('|')
      for item in items:
        if item != '*':
          print(item)
    else:
      print(match.group(1))
