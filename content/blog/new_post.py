#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PURPOSE: Create a new post
AUTHOR: Dylan Gregersen
DATE: Wed Oct 29 11:03:40 2014
"""
# ########################################################################### #

# import modules 

from __future__ import print_function, division, unicode_literals
import os
import sys 
import io
import datetime 
import time

PY3 = sys.version_info.major == 3

if not PY3:
    input = raw_input

# ########################################################################### #
boiler = """title: {title}
date: {date}
template: article
authors: Dylan Gregersen
status: draft # published
comments: true
category: 
tags: 
- 
summary:

content

"""




title = input("title: ").replace(" ","-")
now = datetime.datetime.now()
filename = "{year}-{month}-{day}-{title}.md".format(year=now.year,month=now.month,
    day=now.day,title=title)

kws = dict(\
    title=title,
    date=time.ctime(),    
    )
fp = os.path.join(str(now.year),filename)
with io.open(fp,'w') as f:
    f.write(boiler.format(**kws))
print("created:\n"+fp)
