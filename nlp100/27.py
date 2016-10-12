#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 27.py
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

lineFlag = False
template = {}
for line in country['text'].split("\n"):
  if lineFlag:
    if re.match(r"}}", line) != None:
      lineFlag = False
    else:
      match = re.match(r"\|(.+) = (.+)", line)
      if match != None:
        template[match.group(1)] = match.group(2)
      else:
        pass
  else:
    if re.match(r"{{基礎情報", line) != None:
      lineFlag = True

for k, v in template.items():
  if '\'' in v:
    v = v.replace("'", "")
  if "ファイル" in v:
    v = re.match(r"\[\[....:(.+)\|", v).group(1)
  if '<' in v:
    vtemp = v.split("<")
    v = vtemp[0]
  if '[' in v:
    v = v.replace("[", "")
  if ']' in v:
    v = v.replace("]", "")
  if '{' in v:
    v = re.match(r"{{lang\|..\|(.+)}}", v).group(1)
  if "|" in v:
    vtemp = v.split("|")
    v = vtemp[1]
  template[k] = v
  print(k, template[k])

print(template)
