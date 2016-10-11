#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 21.py
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
  if re.search(r"Category", line):
    print(line)
