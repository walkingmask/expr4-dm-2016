#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 24.py
# 2016/10/12(水)
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
  match = re.search(r"(File|ファイル|Media):(.+\.)(png|gif|jpg|jpeg|xcf|pdf|mid|ogg|svg|djvu)\|", line, re.IGNORECASE)
  if match != None:
    print(match.group(2)+match.group(3))
