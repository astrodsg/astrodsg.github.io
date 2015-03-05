title: How I Made My Blog
date: Wed Mar  4 09:41:09 2015
template: article
authors: Dylan Gregersen
status: draft
comments: true
category: Programming 
tags: 
- blog
- pelican
- python
- web-dev
summary: This is the obligatory post which all programmers with a home-made blog have to write (Ha).

<br>
<br>

# How I Made My Blog #

When I created this website using Pelican I looked at many other websites and examples (I'm a master google searcher--aren't we all?). I thought I'd avoid writing my own "how I made this blog"; however, a recent conversation with a friend convinced me that at least he would appreciate some notes about my website generator. Hence the reason for this post.

# Pelican #

When I started, I wanted to host at github which only posts static content. Github uses [Jekyll](https://help.github.com/articles/using-jekyll-with-pages/) as their static content generator. I tired it out but decided to use [Pelican](http://docs.getpelican.com/en/3.5.0/) instead. I changed primarily because I know Python and not Ruby. I picked Pelican in particular after looking at many "Best Static Generator" reviews which ranked it high. So far I've been happy with this choice.

# Getting Up and Running #

By and large I put together this website by parsing through and following the [official Pelican getting started](http://docs.getpelican.com/en/3.5.0/). Their walk through is pretty good and I suggest using it to get going.

<hr>

## Install Pelican ##

First you need the pelican code which can be installed simply with [pip](https://pip.pypa.io/en/latest/). Also checkout the [Installing Pelican](http://docs.getpelican.com/en/3.5.0/install.html) page which gives some more help with setting up pelican in a virtualenv (Recommended).

    pip install pelican markdown

Choose a directory on your computer to put all the files

    mkdir -p ~/projects/yoursite
    cd ~/projects/yoursite

In the new directory run `pelican-quickstart`. 

    pelican-quickstart

The quickstart asks some questions. I recommend Y for the Fabfile/Makefile and auto-reload script. The "Do you want to upload" will set up more destinations to put in the Makefile; you can add them manually later.

## Set Up Directory Structure ##

The beauty of a static website generator is the separation of content (stuff you write) from the layouts and styles (html/css/javascript). The generator compiles all the stuff together into your html pages which can then be hosted. 

First, structure of your content directory (within your "~/project/yoursite" directory). I wanted a website that was not entirely blog focused (which is not the default) so I structured my website and content directory:

    website/
    ├── content
    |   ├── README.md
    │   ├── blog/   # blog posts
    |   |   ├── 2014/
    |   |   |   ├── 2014-1-1-example_blog_post.md
    |   |   |   └── ... 
    │   │   └── ...
    │   ├── pages/  # web pages which are not blog post
    |   │   ├── blog.md
    │   │   ├── about.md
    |   │   ├── direct/
    |   │   |   └── ... more on this later
    |   │   └── ...
    |   |   
    |   └── static/
    |       ├── css/  # custom css which doesn't belong to the theme
    │       │    ├── blog/
    │       │    │   ├── 2014-1-1-example_blog_post.css
    │       │    │   └── ... 
    |       │    └── ... 
    |       ├── files/  # static files to download
    |       ├── img/    # images associated with webpage
    |       └── js/     # custom javascript which doesn't belong to the theme
    ├── themes/
    │   └── ... # more on this later
    ├── plugins/
    │   └── ... # more on this later
    ├── pelicanconf.py
    ├── publishconf.py
    ├── Makefile
    ├── fabfile.py 
    ├── develope_server.sh
    └── README.md
  


## Add Content ##

To add a post you put a new file into the blog directory

    edit content/blog/2014/2014-1-1-example_blog_post.md

The basic parts of these files are a header and content. The header is the first few lines which give info about the file; the content follows after a few blank lines.

My markdown example:

    title: Example
    date: Wed Jan  1 0:0:0 MST 2014
    template: article
    authors: Me
    status: published
    comments: true
    category: programming
    tags: pelican, python, blog
    
    write your content in _Markdown_!

__Quick Notes__: 

* don't add a space between the keyword and ':' (e.g. "title:" NOT "title :"). This took me a while to figure out cause the default doesn't parse this well.
* status can be 'published' or 'draft'
* tags must be comma separated (unless you do your own shenanigans). 

For rst posts and more information check out the [Pelican Writing Content](http://docs.getpelican.com/en/3.5.0/content.html) page.

My blog.md example:

    edit content/pages/blog.md

    title: My Blog
    date: Wed Jan  1 0:0:0 MST 2014
    modified: Wed Mar  4 13:46:52 MST 2015
    template: archives
    
    # Welcome to my Blog #
    
    Here I like to talk about stuff. 


## Website Settings ##

In a moment we'll make your new website but first we need some stuff in the 'pelicanconf.py' file. Open up with your favorite editor. Check and define the following global variables based on the structure above:

    PATH = 'content'
    OUTPUT_PATH = 'output'
    STATIC_PATHS = [\
        'README.md',
        'blog',
        'static/img',
        'static/css',
        'static/js',        
        'static/files',            
        ]
    PAGE_PATHS = ['pages']
    ARTICLE_PATHS = ['blog']
    ARTICLE_URL = 'blog/{category}/{date:%Y}/{date:%m}/{slug}.html'
    ARTICLE_SAVE_AS = 'blog/{category}/{date:%Y}/{date:%m}/{slug}.html' 

These make sure that Pelican knows where all our content lives and where it should go. More on the `pelicanconf.py` in a sec


### Publish/View Your Website ###

Finally, let's get a little dev server up and running. This happens to be as simple as 

    make devserver

A bunch of log messages pop up (fix any errors if present). Then in a web browser (like Firefox) go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

__Note__: the devserver keeps track of some changes to the files. However, I found that it's not always very good at updating the right stuff. So I often have to re-type `make devserver` to force a recreation of the website.


<hr>
<hr>











## Changing the Theme ##

You can try out styling your website. Check out [example themes](http://www.pelicanthemes.com/), try downloading one into 'templates/<theme_name>'

For example using git.

    

## Pandoc Markdown ##

One head-ache I had with Pelican was with markdown. I decided I wanted to write my blogs in Markdown. In particular, the Pandoc Markdown because of the advanced handling of tables, code feilds, and references. 










