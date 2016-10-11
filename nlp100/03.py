#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 03.py
# 2016/10/05(水)
# walkingmask

import string

bun = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
mojisu=[]
for tango in bun.replace(',','').replace('.','').split(" "):
  mojisu.append(len(tango))
print(mojisu)
