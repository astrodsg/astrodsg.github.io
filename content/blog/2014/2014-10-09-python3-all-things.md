title: Python 3 All the Things!
date: Thu Oct 09 19:05:59 MDT 2014
authors: Dylan Gregersen
status: published
comments: true
template: article
category: Programming
tags: python, python3, programming, 2to3
summary: I just gave a Python3 talk to [SLCPython Meetup]()
+
Here are some links and resources to find out more about all the hype

<br/>
<br/>

# __Python 3 : A Language for the Future__ #

Yesterday gave a talk at [SLCPython Meetup](http://www.slcpy.com) Group about Python3. When I agreed to give this talk I had already read through many of the pages of changes (e.g. [What's new in Python 3](https://docs.python.org/3.0/whatsnew/3.0.html)) and felt like I had a pretty good understanding of the changes. The thing I didn't realize was how much I would be learning about unicode. 


[Click here for Resources from my talk](https://github.com/astrodsg/Python2to3)

<br/>

# __Why Unicode is a Step Forward__ #

Python 2 had several implicit uses of [ASCII](https://en.wikipedia.org/wiki/ASCII) encoding/decoding. ASCII was the first, widely accepted system for encoding human language (i.e. English) to computer bytes. This process is necessary because humans don't express themselves well in bytes and computers don't do well with language. 

Many human languages exist. Each has its own ways to express ideas. As computers have evolved and become used all around the globe the need for computers to encode/decode more than just English is paramount.  The development of the [Unicode](https://en.wikipedia.org/wiki/Unicode) system characters is a major step to solving this problem. The next step is for developers to implement Unicode as a foundation for computer systems. This step will make computers more accessible to people of all backgrounds and cultures.


<img alt="It's a Unicode Party (Sorry this is mostly white folk, but it's fun gif)" src="{filename}/static/img/blog/its_a_party.gif" style="width: 50%; display: inline-block;"/>
<img alt="Unicode Hello World" src="{filename}/static/img/blog/hello_world_all.png" style="width: 50%; display: inline-block; float:right;"/>

# __Python Adoption of Unicode__ #

Unicode handling is the primary reason for the break in backwards compatibility. In the words of core developer [Nick Coghlan](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html
) "Fixing [Unicode handling bugs] within the constraints of the Python 2 text model is considered too hard to be worth the effort." 

The new text model in Python 3 treats all text as either byte arrays (machine language) or Unicode (human language(s)) with more explicit encoding/decoding. The diagram which helped me was this:


<img src="{filename}/static/img/blog/unicode_sandwich.jpg" alt="Unicode Sandwich" style="width:60%;"/>

On the outside of the sandwich there's the computer and byte storage, on the inside is the Unicode which humans understand. 

This new text model also allows people to write code using any Unicode character. For example, [these scripts](https://github.com/renyuanL/pythonTurtleInChinese) published on github use chinese characters (pretty fracking cool).

# __Fixing Up Loose Ends__ #

Since the core developers broke backwards compatibility anyway, this has been a great opportunity to fix up many of the inconsistencies and gotcha's of Python 2. These are the changes most of us will notice. Things like maing `print` a function or the deprecation of many functions and class methods (like `raw_input` or `dict.iterkeys`). 

I found it useful to look online at several of the "what's new guides". I think [Brian Curtin's Porting Guide](http://docs.pythonsprints.com/python3_porting/py-porting.html) is a nice and succinct place to start.

--------

<img alt="Python3 Wants You" src="{filename}/static/img/blog/Python3_wants_you.png" style="margin-top:80px; margin-bottom: 30px; height: 20%;"/>


# __Now is the Time!__ #

Python is a powerful language mostly because of it's libraries build by the community. The fear was that these packages would have trouble converting to Python3 (maybe never do) and that would be the end of Python. However, it seams to me that fear is no longer valid. By several measures, we're now at 75% support of Python3 by major libraries. One of these measures, is the [Python 3 Readiness](http://py3readiness.org/) site which looks at the top 360 `pip` packages and the adoption of Python3.


<a href="http://py3readiness.org/">
<img alt="Python3 Readiness" src="{filename}/static/img/blog/Python3_Readiness.png"/>
</a>

With almost all major libraries now supporting Python 3, it's up to the rest of us to adopt this new language. Good luck!

# Other Online Materials #

* [What's New in Python 3](https://docs.python.org/3.0/whatsnew/3.0.html) – for most of the Python 2.7 to Python 3 changes.
* [What's New](https://docs.python.org/3/whatsnew/) – for a VERY long list of everything new (though check out the dense but "short" summary)
* [Pragmatic Unicode talk/essay](http://nedbatchelder.com/text/unipain.html) – or "Why Python 3 Exists" - Coghlan
* [Python 3 Porting Guide](http://docs.pythonsprints.com/python3_porting/py-porting.html) – nice quick reference for things which have changed from 2.x to 3x
* [Porting to Python 3: An in-depth guide](http://python3porting.com/) – Definitely in depth



