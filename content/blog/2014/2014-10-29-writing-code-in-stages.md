title: When Coding, Write in Stages
date: Wed Oct 29 11:42:19 MDT 2014
authors: Dylan Gregersen
status: draft
comments: true
template: article
category: Astronomy
tags: python,interactive,research,tips-n-tricks
summary: Basically it's best to write code which will execute in stages


Basically this post is about caching your results as you go. Why it's a fantasitic idea and how I do it. 

This was a lesson I learned while writing scripts for my Astronomy research. I like to have all my code for a particular task in one script. I haven't really given up on that because I think it's good to have all the logic in one place. However, I learned the importance of coding in stages so that I don't have to continually re-run code which takes a long time. 

# Working in Stages

Don't write one code which runs from start to finish. Segment your code into functions and sections which can be run one at a time.

Here's an example. I have a script which processes some data and makes plots of it. The "bad" way is to write a script which generates goes back and forth running processing steps (which take a while) and adding data to my plots. 



 I have some function which generates data to plot. This function takes, say an hour to run. Then I make a plot with the data. Often these two tasks are lumped together (cause it makes logical sense) but from the CS viewpoint this makes the process harder. Say you want to change parameters of the plot or there's an error in your plotting. Then you must re-run the entire code just to fix those minor bugs.

### Solution 1: Make two scripts

Make two scripts. One which generates the data and saves to file. Another which reads the data and makes a plot. 

### Solution 2: Cache Results in Memory

I still like to have all my code together in one script so I break up my code into two functions: One which generates the data; another which plots it.

In a script (example.py) I have the two lines:
    data = function(input)
    plot_data(data,filename_out)

Then I use execfile to execute interactively
    >>> execfile("example.py")
    >>> 

To re-run and just make the plot I comment the data line out and re-execute in the open terminal.
    # data = function(input)
    plot_data(data,filename_out)

This method works because I don't close the python terminal. I'm using it interactively so the terminal still knows what 'data' means and keeps it all around in memory. The same works for this:

    if 'startup' in globals():
        ...
        data = function(input)
        ...
        startup = True
    plot_data(data,filename_out)

The variable `startup` lets the code know that that block has been run in the current terminal and all the names are saved in the current session.

### Solution 3: Use a Function Cacher

Allow the function or some object to store the results of running something long and interactive.


## Python 3

Of the changes in Python 3 the one which caused the most distruption to this workflow is the removal of `execfile`. Many posts exist on how to backport `execfile` though I found most didn't work well. This method did, and I've added it to my [python startup file](https://docs.python.org/2/using/cmdline.html#envvar-PYTHONSTARTUP):

    import sys
    import os
    PY3 = sys.version[0] == "3"
    if PY3: 
        # backport of execfile
        def execfile(filepath,  globals=None, locals=None):
            if globals is None:
                globals = sys._getframe(1).f_globals
            if locals is None:
                locals = sys._getframe(1).f_locals
            with open(filepath, "r") as f:
                # import runpy
                # result = runpy.run_path(f,globals,locals)
                # globals.update(result) ??  
                code = compile(f.read()+"\n",os.path.abspath(filepath),'exec')
                exec(code,globals,locals)
        # backport of reload       
        def reload(some_module):
            import importlib as imp
            imp.reload(some_module)
            return(some_module)     

Note the reason `execfile` was deprecated is because it's not the correct thing to use to incorporate other code into your scripts. I.e. In a script never do:

    ...
    execfile("other_script.py")
    ...

Always use `import other_script`. If you change something in 'other_script' you'll need to `reload(other_script)`.


















