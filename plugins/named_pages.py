#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PURPOSE: 
AUTHOR: Dylan Gregersen
DATE: Sun Nov 23 16:04:35 2014
"""
# ########################################################################### #

# import modules 

from __future__ import print_function, division, unicode_literals
import io
import os 
import sys 
import re 
import time
import pelican 
from pelican import signals
from pelican import contents

def add_pages_by_name (page_gen):
    pages_by_name = {}
    for page in page_gen.pages:
        if hasattr(page,'name'):
            pages_by_name[page.name] = page
    page_gen.context['pages_by_name'] = pages_by_name 

def register():
    signals.page_generator_finalized.connect(add_pages_by_name)

    
