#!/usr/bin/env python
"""
PURPOSE: For custom tag cloud parameters
AUTHOR: Dylan Gregersen
DATE: Sun Nov 23 16:04:35 2014
"""
# ########################################################################### #

# import modules
import io
import os
import sys
import random
import math
import re
import time
import pelican
from pelican import signals
from pelican import contents
from collections import defaultdict
from operator import attrgetter, itemgetter



def generate_custom_tag_cloud (article_gen):
    # create tag cloud
    tag_counts = defaultdict(int)
    for article in article_gen.articles:
        for tag in getattr(article, 'tags', []):
            tag_counts[tag] += 1
    if not len(tag_counts):
        return 

    # sort the tag cloud
    tag_cloud_sort_key = eval(article_gen.settings.get("TAG_CLOUD_SORT_KEY","lambda item:int(item[1])"))
    tag_counts = sorted(tag_counts.items(), key=tag_cloud_sort_key, reverse=True)

    # select a maximum number of items
    tag_counts = tag_counts[:article_gen.settings.get('TAG_CLOUD_MAX_ITEMS')]
    counts = map(itemgetter(1),tag_counts)

    # function to scale the counts by
    tag_cloud_scale_fxn = eval(article_gen.settings.get("TAG_CLOUD_SCALE_FXN","None"))
    if tag_cloud_scale_fxn is None:
        steps = article_gen.settings.get('TAG_CLOUD_STEPS',len(set(counts)))
        tag_cloud_scale_fxn = lambda x,counts: int(math.floor(steps-(steps-1)*math.log(x)/(math.log(max(counts) or 1))))

    tag_cloud = []
    for tag,count in tag_counts:
        tag_cloud.append((tag,tag_cloud_scale_fxn(count,counts)))

    if article_gen.settings.get('TAG_CLOUD_RANDOMIZE',False):
        # put words in chaos
        random.shuffle(article_gen.tag_cloud)

    article_gen.context['tag_cloud'] = tag_cloud 

def register():
    signals.article_generator_finalized.connect(generate_custom_tag_cloud)





