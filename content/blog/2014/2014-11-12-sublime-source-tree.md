title: Sublime Text and SourceTree
category: Programming 
date: Wed Nov 12 15:54:33 MST 2014
authors: Dylan Gregersen
status: draft
comments: true
template: article
tags: git, SourceTree, SublimeText, workflow
summary: How to make Sublime Text your default diff editor for SourceTree

# Integrating Sublime Text and SourceTree #

I've recently adopted [Sublime Text](http://www.sublimetext.com/) as my primary editor and am loving it. The package [Sublimerge](http://www.sublimerge.com/) is fantastic for looking at file differences and has awesome integration for git. 

Source Tree is a nice GUI for git. I know some purists only use command line git and I can respect that. I enjoy the having the the GUI to easily scan through and view changes in files. 

Source Tree has integration for viewing file differences in an external application. You just 

I use SourceTree to view and compare git versioning

I use Sublime Text as a default text editor

I purchased/installed Sublimerge Packages

    ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/bin

Diff Command:

/usr/bin/subl
--new-window --wait "$REMOTE" "$LOCAL" --command "sublimerge_diff_views {\"left_read_only\": true, \"right_read_only\": true}"

Merge Command:

/usr/bin/subl
--new-window --wait "$REMOTE" "$BASE" "$LOCAL" "$MERGED" --command "sublimerge_diff_views" 
