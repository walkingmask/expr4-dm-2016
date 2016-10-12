#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 29.py
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

import urllib.request

url = "https://commons.wikimedia.org/w/api.php?action=query&titles=File:"+template["国旗画像"]+"&prop=imageinfo&iiprop=url&format=json"
url = url.replace(" ", "%20")
try:
    response = urllib.request.urlopen(url)
    content = json.loads(response.read().decode('utf-8'))
finally:
    response.close()

for k in content["query"]["pages"].keys():
  print(content["query"]["pages"][k]["imageinfo"][0]["url"])
