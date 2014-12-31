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

def generate_article (gen,filepath):
    """ Use some generator to read an article filepath and return the
    article object 

    """
    article = gen.readers.read_file(\
        base_path=gen.path,
        path=filepath,
        content_class=pelican.contents.Article,
        context=gen.context,
        preread_signal=signals.article_generator_preread,
        preread_sender=gen,
        context_signal=signals.article_generator_context,
        context_sender=gen,
        )
    return article 

def slot_include_articles (pel):
    """
    Method to create a variable `include_articles` in 
    the pelican.settings which can be used in templates

    `include_articles` is a list of article objects. Each article object has
    an attributed attached called `include_content` which has all content 
    excluding the metadata 

    """
    pel.settings['include_articles'] = {}

    context = pel.settings.copy()
    # Share these among all the generators and content objects:
    context['filenames'] = {}  # maps source path to Content object or None
    context['localsiteurl'] = pel.settings['SITEURL'] 

    filepaths = context.get("INCLUDE_ARTICLES",None)
    if filepaths is None:
        return 

    gen = pelican.generators.ArticlesGenerator(\
        context = context,
        settings = pel.settings,
        path = pel.path,
        theme = pel.theme,
        output_path = pel.output_path,
        )

    for fp in filepaths:
        article = generate_article(gen, fp)
        pel.settings['include_articles'][fp] = article

def register():
     signals.initialized.connect(slot_include_articles)

    
