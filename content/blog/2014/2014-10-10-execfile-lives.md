title: Execfile Lives!
date: Fri Oct 10 19:05:59 MDT 2014
authors: Dylan Gregersen
status: published
comments: true
template: article
category: Programming
tags: python, python3, programming, workflow
summary: Reviving `execfile` for Python 3 

# Execfile Lives!

One of the changes in Python 3 is the deprecation of the builtin function `execfile`. This was done with very good intentions and lots of thought. I mostly agree with the choice but here's why I choose to resurrect...`execfile`.

## Deprecating `execfile` was Good

<!-- First off, `reload` was just taken out of the main namespace. You can still access it using `from importlib import reload`. I'm not exactly sure the reason (if you know please comment), but most likely it was to clean up the main python namespace. Modules will automatically be loaded each time you run a script afresh. Most of the time this is enough and requiring a developer to go to the standard library package importlib is nice. 
 -->
 `execfile` takes a file, compiles it into a code object (under the hood), and executes each line of code in turn every time it's called. At one point, I used this in the way feared by the core Python developers: to include other code. I have two files "file1.py" and "file2.py"; I want to include "file1.py" into "file2.py" to execute the lines; So I do the following:

"file2.py"
```python
...
execfile("file1.py")
...
```

*THIS IS BAD!* Primarily because you have no idea what variables in "file1.py" are now in the current namespace. It makes it hard to read and debug. 

To include extra code correctly you should locate "file1.py" into your PYTHONPATH and use `import file1` to access all the variables. You can use `imp.reload` if you want to interactively update data from the file

## Deprecating `execfile` was Bad and how to Resurrect

__Entirely for interactively use.__ For my research, I primarily use Python as an interactive shell to type in the commands I want executed then dynamically investigate the results. I explicitly type `execfile` onto the command line so that it will be executed in the interpretor and all the variables will be in the main namespace. Then I can segment parts of the script to put into other scripts which I can import.

A few different methods have been discussed on other blogs. The ones I found lead me on the right track but required a few modifications. The method below was what finally worked for me. I've included it in my PYTHONSTARTUP file with a conditional checking `sys.version[0] == "3"`.

```python
def execfile(filepath,  globals=None, locals=None):
    import sys
    if globals is None:
        globals = sys._getframe(1).f_globals
    if locals is None:
        locals = sys._getframe(1).f_locals
    with open(filepath, "r") as f:
        try:
            code = compile(f.read()+"\n",os.path.abspath(filepath),'exec')
            exec(code,globals,locals)
        except KeyboardInterrupt:
            return
```

Hope this helps!



