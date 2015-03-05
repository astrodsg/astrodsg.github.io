title: Publishing a Pelican Project to Github Pages
date: Wed Mar  4 19:37:15 2015
template: article
authors: Dylan Gregersen
status: published
comments: true
category: programming 
tags: 
- python
- pelican
- git
- web-dev
- github
summary: I wanted to create a static website using Pelican and publish to my astrodsg.github.io github page. With a created a Pelican project this describes how to set up git and a method for pushing to the remote master branch. 


# Publishing Pelican to Github Pages #

When I created my personal webpage, I planned for it to be git tracked and hosted on github pages. I used Pelican to generate the static content to push to github. Reading up on [Github Pages](https://pages.github.com/) I learned they want me to push to "username.github.io, where username is your username (or organization name) on GitHub". But the unexpected trick was that when github's server looks at http://username.github.io it uses the master branch. 

This post is about how I set up my Pelican website with git and published to http://username.github.io master branch. 

## Tracking Your Pelican Project with Git ## 

If you have some pelican project going this will add git version control. My example lives in "~/project/yoursite". 


First, create and add the following lines to "~/project/yoursite/.gitignore"

    publishconf.py 
    output
    *.pyc
    *.pid
    cache
    __pycache__

Next, initialize git

    cd ~/project/yoursite/  # directory of our pelican project
    git init
    git add .
    git commit -m "initial commit"

You'll want to familiarize yourself with git if you haven't already. 

## Set Up Pelican to Publish to Github Pages ## 

Now I'll walk through setting up your Pelican project to be your primary github page. Github hosts, for free, websites with static content (explained at [Github Pages](https://pages.github.com/)). You can create sub-websites for each project and one primary for your account. The primary account is located at username.github.io "where username is your username (or organization name) on GitHub". 

To set up your project on github, create the repo on github then run

    git remote add origin https://github.com/username/username.github.io # where username is your username (or organization name) on GitHub.

When you create your username.github.io repository github hosts the content on your master branch. But now there's **a problem:** But your master branch is also where all your pelican development is and the what you want to publish is probably in an output directory. 

**My solution:** Have my primary development in a branch called pelican and then push my final content to the master. This is not standard but I think it's pretty elegant. 

To implement create a second branch (your new master) called 'pelican' (or whatever you actually want to use)

    git checkout -b pelican


Now to push to the master branch their's a handy tool called ghp-import. You can install via pip:

    pip install ghp-import

If you've set up pelican project with a Makefile (recommended) then you can simply edit that file by adding:

    GITHUB_PAGES_BRANCH=master

If not you can create a make file and add the following:

    OUTPUTDIR=output
    GITHUB_PAGES_BRANCH=master
    github: publish
        ghp-import -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
        git push origin $(GITHUB_PAGES_BRANCH)

Now when you type `make github`, it'll make the pelican content out to the master branch and push it to github. Then you can go to [https://username.github.io] to view your website from anywhere! Nifty, huh?


