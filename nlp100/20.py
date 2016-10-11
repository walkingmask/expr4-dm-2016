#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 20.py
# 2016/10/11(火)
# walkingmask

import json

# load json data from file
articles = []
for line in open("jawiki-country.json", 'r'):
  articles.append(json.loads(line))

# U.K.
for country in articles:
  if country['title'] == 'イギリス':
    break

print(country['text'])
