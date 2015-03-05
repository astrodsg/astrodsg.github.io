title: Supermongo to Python
date: Sat Oct 25 19:05:59 MDT 2014
authors: Dylan Gregersen
status: published
comments: true
template: article
css: static/css/supermongo-to-python.css
category: Astronomy
tags: astronomy, plotting, python, supermongo
summary: __Paper : Rock__ as __Python : Supermongo__
+
A tutorial for switching from Supermongo to Python

# Supermongo to Python Matplotlib #

## Introduction ##

Supermongo (SM) is a domain-specific programming language for creating plots. It was first written in 1987. Astronomers adopted this language as a primary plotting package for data analysis. Many groundbreaking discoveries have been seen using supermongo plots. However, new tools exist for plotting which have evolved from first plotting languages like Supermongo. These new tools provide methods for creating plots with fewer lines of code. They provide better integration into other programming languages and code.

Matplotlib is a domain-specific plotting library for the general-purpose programming language Python. This library provides all the plotting capabilities of Supermongo and more. This post is to provide a 1-to-1 guide for Supermongo experts to apply their knowledge in Python with Matplotlib.

Other Python plotting packages include : bokeh, plotly, vispy

<!-- __TODO: outline__

[General Comparison ](##General-Comparison)
[Getting Started With Supermongo-Python](##Getting-Started-With-Supermongo-Python)
 -->

------------------------------------------------------

## General Comparison ##

__Variables:__ In Supermongo all variables are global so wherever you change them, within any macro, they change everywhere else. In Python variables have scope. You can use the same variable name in mulitple functions and be sure that they will act independantly.

__Plot States:__ In Supermongo you have a single plot state which you update with the interactive commands. Matplotlib also uses a plot state which you edit with commands.

__Object Oriented:__ Supermongo is a procedural programming language. You write out all the steps and they execute in that order. Python is object oriented meaning you can create data objects and write them into procedures. This method is how your operating system is built and is extremely useful.

__Community Support:__ If you've ever searched the internet for help with Supermongo (chances are you have if you're reading this) you've come across a handful of useful sites: The [SM manual](http://www.astro.princeton.edu/~rhl/sm/), [Annika Peter's Guide](http://www.astro.caltech.edu/~apeter/sm/basic.html), [Craig Rudick's Tutorial](http://astroweb.astr.cwru.edu/craig/sm/plot_sm.html) and [Rebecca Stanek's Guide](http://www.rebeccastanek.com/super/). These resources and only a few others are the mainstay of the Supermongo online support. 

By contrast the community supporting Matplotlib is immense. Not only is it developed by many people to have lots of functionality, it also has a large user base. If you are unsure how to make some plot thing, a quick internet search often pulls up many solutions. 
<!-- TODO look up main matplotlib repo -->


## Python requirements ##

Because general purpose language you'll need specific subpackages. For this tutorial:

* maplotlib
* numpy

Hopefully, these packages came with your installation of Python. You can also install them using the command line utility `pip` (e.g. `pip install numpy`)
This tutorial will work with both Python 2 and 3. 

<br/>
<br/>
<br/>

------------------------------------------------------

## Getting Started ##

### Working interactively ###

In Supermongo all your plotting is done either interactively (you type and the plot is modified) or using a script. In Python you do the same.

To use the interactive mode, on the command line type `python` (better yet try out `ipython` for more interactive fun). Now you should have a new prompt, probably with '>>>' which you type your python code. (Check out TODO for a python tutorial)

```python
import numpy as np  
x = np.array(10)  
# comment
for i in range(len(x)):
    """ String doc """
    print(" value {} = {}".format(i,x[i]))
```

Here's a side by side comparison of interactive mode. 

+--------------------+------------------------------------+
|     Supermongo     |               Python               |
+====================+====================================+
| ```supermongo      | ```python                          |
| div X11            | from matplotlib.pylab import *     |
| set x = {2,3}      | x = [2,3]                          |
| set y = {5,10}     | y = [5,10]                         |
| con x y            | plot(x,y)                          |
| xlabel time        | xlabel("time")                     |
| ylabel temperature | ylabel("temperature")              |
|                    | show() # not necssary if run ion() |
| ```                | ```                                |
+--------------------+------------------------------------+

__NOTE:__ The remainder of the tutorial I don't use `from matplotlib.pylab import *` and instead use `import matplotlib.pylab as plt` then commands like `plt.plot`. The reason has to do with how many named things there are and to allow me to make my own `plot` function different from the default `plt.plot` function. Basically, it's good coding practice. 

### Writing Scripts ###

Both languages allow you to write a script to execute commands. If you're not doing this you really should. In a nut shell, you just write the lines you would type into the interactive mode into a text file and then execute that file. You will want to use [Emacs](https://www.gnu.org/software/emacs/), [Sublime Text](http://www.sublimetext.com/), [TextWrangler](http://www.barebones.com/products/textwrangler/) or some equivalent text editor.

With Supermongo you write a script with at least one macro, for example:

__"script.sm"__
```supermongo 
main_macro 
    dev x11
    ctype white
    set x=0.0,10.0,1.0
    set y=x**2
    lim x y 
    box
    con x y
```

Then startup Supermongo using `sm` enter `macro read script.sm` and then `main_macro` to execute.

For Python you write a script similarly 

__"script.py"__
```python
import matplotlib.pylab as plt
import numpy as np

x = np.arange(0.0,10.0,1.0)
y = x**2
plt.plot(x,y)
plt.show()
```

Then you can run it with `python script.py` or open it interactively using `python` and write `execfile("script.py")`. *Note:* In Python 3, they deprecated execfile. See my post [Execfile Lives!]({filename}blog/programming/2014/10/execfile-lives.html) for more info.

<br/>
<br/>
<br/>

------------------------------------------------------

## Comparisons of Supermongo and Python Plotting ##

Plotting libraries implement functions to display views of data. One of the basic views is comparing one data parameter (say X) against another (say Y) and just plotting the intersecting points (a.k.a. a scatter plot). In this section, I make direct comparisons of Supermongo to Python plotting methods. 

### Adding items to plots ###

Both plotting packages create some plot axes which you can then add views of your data to. 


Both plotting packages have methods for adding XY data as lines, points, and with errorbars. Below is the side by side comparison. 


+-------------+------------------+--------------------------------------------+
|     Task    |    Supermongo    |                   Python                   |
+=============+==================+============================================+
| Plot lines  | ```supermongo    | ```python                                  |
|             | connect x y      | plt.plot(x,y)                              |
|             | ```              | ```                                        |
+-------------+------------------+--------------------------------------------+
| Plot line   | ```supermongo    | ```python                                  |
|             | line x1 y1 x2 y2 | plt.plot([x1,x2],[y1,y2])                  |
|             | ```              | ```                                        |
+-------------+------------------+--------------------------------------------+
| Plot line   | ```supermongo    | ```python                                  |
|             | relocate x1 y1   | plt.plot([x1,x2],[y1,y2])                  |
|             | draw x2 y2       |                                            |
|             | ```              | ```                                        |
+-------------+------------------+--------------------------------------------+
| Plot points | ```supermongo    | ```python                                  |
|             | points x y       | plt.scatter(x,y)                           |
|             |                  | # or use                                   |
|             |                  | plt.plot(x,y,linestyle='none')             |
|             | ```              | ```                                        |
+-------------+------------------+--------------------------------------------+
| Error bars  | ```supermongo    | ```python                                  |
|             | errory x y yerr  | plt.errorbar(x,y,yerr=yerr)                |
|             | errorx x y xerr  | plt.errorbar(x,y,xerr=xerr)                |
|             |                  | plt.errobar(x,y,xerr=xerr,yerr=yerr)       |
|             | ```              | ```                                        |
+-------------+------------------+--------------------------------------------+
| Horizontal  | ```supermongo    | ```python                                  |
| Line        | hzline y         | plt.axhline(y)                             |
|             | ```              | ```                                        |
+-------------+------------------+--------------------------------------------+
| Vertical    | ```supermongo    | ```python                                  |
| Line        | vtline x         | plt.axvline(x)                             |
|             | ```              | ```                                        |
+-------------+------------------+--------------------------------------------+
| Rectangle   | ```supermongo    | ```python                                  |
|             | relocate x1 y1   | rec = plt.Rectangle(x1,y1,(x2-x1),(y2-y1)) |
|             | draw x1 y2       | plt.gca().add_patch(rec)                   |
|             | draw x2 y2       |                                            |
|             | draw x2 y1       |                                            |
|             | draw x1 y1       |                                            |
|             | ```              | ```                                        |
+-------------+------------------+--------------------------------------------+


+-----------+-------------------------+------------------------------------+
|    Task   |        Supermongo       |               Python               |
+===========+=========================+====================================+
| Images    | ```supermongo           | ```python                          |
|           |                         | x = np.ones((10,10))               |
|           | Unknown, please comment | plt.image(x)                       |
|           |                         | # or use                           |
|           |                         | xcoord = np.linspace(0,5,20)       |
|           |                         | ycoord = np.linspace(-3,3,10)      |
|           |                         | z = np.ones((20,10))               |
|           |                         | ax = plt.figure().add_subplot(111) |
|           |                         | ax.pcolorfast(xcoord,ycoord,z)     |
|           | ```                     | ```                                |
+-----------+-------------------------+------------------------------------+

<!-- | Histogram | supermongo           | python                          |
|           | set bins xmin,xmax,step | bins = np.arange(xmin,xmax,step)   |
|           |                         |                                    |
|           |                      |                                 |
 <small>Thanks to http://www.rebeccastanek.com/super/ </small> -->




+------------------+------------------------+--------------------------------+
|       Task       |       Supermongo       |             Python             |
+==================+========================+================================+
| X-axis Label     | ```supermongo          | ```python                      |
|                  | xlabel label_name      | plt.xlabel("label_name")       |
|                  | ```                    | ```                            |
+------------------+------------------------+--------------------------------+
| Y-axis Label     | ```supermongo          | ```python                      |
|                  | ylabel label_name      | plt.ylabel("label_name")       |
|                  | ```                    | ```                            |
+------------------+------------------------+--------------------------------+
| Title Label      | ```supermongo          | ```python                      |
|                  | toplabel title_of_plot | plt.title("title_of_plot")     |
|                  | ```                    | ```                            |
+------------------+------------------------+--------------------------------+
| Add Text to Plot | ```supermongo          | ```python                      |
|                  | relocate x y           | plt.text(x,y,"label_text")     |
|                  | label label_text       |                                |
|                  | ```                    | ```                            |
+------------------+------------------------+--------------------------------+
| Annotations      | ```supermongo          | ```python                      |
|                  | relocate x y           | plt.annotate(x,y,"label_text") |
|                  | label label_text       | # use keywords for annotate    |
|                  | # draw arrows or       | # to easily add arrows to data |
|                  | # additional items     |                                |
|                  | ```                    | ```                            |
+------------------+------------------------+--------------------------------+

Plot legends are a pain in Supermongo. If you want a bounding box you need to draw the rectangle yourself specifying every corner. Then you have to specify the exact positions of each label, draw a point with the correct styles at the correct location, then add the text slightly offset. If you want to add/remove
labels or if points styles change then you're often thrown into chaos. (Of course you can write macros, but why? when Python makes it so easy!)

The python `plt.legend` function looks for any plot item you added a lable=? keyword argument to. This includes all lines and points as well as patches like plt.Rectangle and plt.Circle. It's also easy to manipulate the position using the loc=? keyword of `plt.legend`.

+-------------+----------------------+----------------------------------+
|     Task    |      Supermongo      |              Python              |
+=============+======================+==================================+
| Plot Legend | ```supermongo        | ```python                        |
|             | # Draw Rectangle box | # just add label keyword         |
|             | relocate xpt= ypt    | # to your plot call              |
|             | # Set ptype,ctype    | plt.plot(x,y,label="Item Label") |
|             | dot                  | plt.legend()                     |
|             | relocate xpt+dx ypt  | # use help(plt.legend) to find   |
|             | label Item Label     | # out about keywords             |
|             | ```                  | ```                              |
+-------------+----------------------+----------------------------------+


### Controlling Plot Styles ###

In Supermongo you must set the styles globally before adding them to the plot. This can lead to frustrating bugs if their out of order

This one may or may not be red points:

```supermongo
points x y 
ctype red
```

This causes the points to be red:

```supermongo
ctype red
points x y
```

In Python you set the plot parameters at the same time you add the item. You do this using keywords in the function call.

```python
plt.scatter(x,y,c='red')
```

You can find out about all the keywords by typing `help(plt.scatter)` in the Python terminal or by using an internet search (the internet is your friend).
*Caveat:* Matplotlib has an rc file that sets some global variables. You can learn more about it [here](http://matplotlib.org/users/customizing.html).

Alright, here comes the one to one of common styles you'll want to manipulate. The Python answers I'm going to use the most common function; Note though, Matplotlib has some inconsistencies with names and so you should refer to the internet or help if you run into problems in your own implementation.

+-------------+---------------+-------------------------------+
|     Task    |   Supermongo  |             Python            |
+=============+===============+===============================+
| Point Color | ```supermongo | ```python                     |
|             | ctype red     | plt.scatter(x,y,c='r')        |
|             | points x y    | # hex colors work             |
|             |               | plt.scatter(x,y,c='#DC322F')  |
|             | ```           | ```                           |
+-------------+---------------+-------------------------------+
| Point Style | ```supermongo | ```python                     |
|             | ptype 10 3    | plt.scatter(x,y,marker='o')   |
|             | ```           | ```                           |
+-------------+---------------+-------------------------------+
| Point Size  | ```supermongo | ```python                     |
|             | expand 1.5    | plt.scatter(x,y,s=100)        |
|             | ```           | ```                           |
+-------------+---------------+-------------------------------+
| Line Color  | ```supermongo | ```python                     |
|             | ctype red     | plt.plot(x,y,color='r')       |
|             | connect x y   | # hex colors work             |
|             |               | plt.plot(x,y,color='#DC322F') |
|             | ```           | ```                           |
+-------------+---------------+-------------------------------+
| Line Style  | ```supermongo | ```python                     |
|             | ltype 2       | plt.plot(x,y,linestyle='--')  |
|             | connect x y   | # or the shortcut             |
|             |               | plt.plot(x,y,ls='--')         |
|             | ```           | ```                           |
+-------------+---------------+-------------------------------+
| Line Width  | ```supermongo | ```python                     |
|             | lw 7          | plt.plot(x,y,lw=7)            |
|             | ```           | ```                           |
+-------------+---------------+-------------------------------+

#### More with Matplotlib ####

In addition to the side by side comparison matplotlib provides you additional ways to plot your data and manipulate your figures.

* [Scatter Points with Color and Size](http://matplotlib.org/examples/shapes_and_collections/scatter_demo.html)
<!-- * [Plot Annotations](http://matplotlib.org/examples/pylab_examples/annotation_demo2.html) -->
* [Arrows](http://matplotlib.org/examples/pylab_examples/fancyarrow_demo.html)
* [2D Histograms](http://matplotlib.org/examples/pylab_examples/hist2d_demo.html)
* [Contours](http://matplotlib.org/examples/pylab_examples/contour_demo.html)
* [2D Images](http://matplotlib.org/examples/pylab_examples/image_interp.html)
* [Box Plots](http://matplotlib.org/examples/statistics/boxplot_demo.html)
<!-- * [Steam Plots](http://matplotlib.org/examples/images_contours_and_fields/streamplot_demo_features.html) -->
<!-- * [Radar Charts](http://matplotlib.org/examples/api/radar_chart.html) -->
* [3D Contours](http://matplotlib.org/examples/mplot3d/contourf3d_demo2.html)
* [Interactive Plots](http://matplotlib.org/examples/widgets/slider_demo.html)
* And much more! Check out the [Matplotlib Gallery](http://matplotlib.org/gallery.html)

### Modifying Plot Properties ###

In addition to add items to a plot you want to manipulate properties of the plot itself. For example, you often want to re-size the bounds of the plot.

It's important to talk about the figure. In Supermongo you only ever have one figure which you can add multiple sub-plots to but usually only one. In Matplotlib you have the option to create multiple figures if you store 


+-----------------+----------------+-----------------------------+
|       Task      |   Supermongo   |            Python           |
+=================+================+=============================+
| Figure          | ```supermongo  | ```python                   |
|                 | page           | fig = plt.figure()          |
|                 | ```            | ```                         |
+-----------------+----------------+-----------------------------+
| Add Plot        | ```supermongo  | ```python                   |
|                 | box            | ax = fig.add_subplot(1,1,1) |
|                 | ```            | ```                         |
+-----------------+----------------+-----------------------------+
| Multipanel Plot | ```supermongo  | ```python                   |
|                 | window 2 2 1 2 | ax = fig.add_subplot(2,2,4) |
|                 | ```            | ```                         |
+-----------------+----------------+-----------------------------+

__Note:__ For Python, storing the plot in `ax` is not necessary but it's a best practice to use matplotlib objects. 

<!-- TODO: add  -->

<br/>

For multipanel plots Supermongo uses the `window` command with arguments __\[*number of columns*\] \[*number of rows*\] \[*x-index*\] \[*y-index*\]__. `window 2 2 1 2` indicates 2 rows 2 columns and the current plot is the bottom-right.

<br/>

In Matplotlib there are several ways to accomplish this (add_subplot,plt.subplots,gridspec). I commonly create a figure `fig = plt.figure()` and add a subplot `ax = fig.add_subplot(1,1,1)`. The arguments are __\[*number of rows*\] \[*number of columns*\] \[*current plot*\]__. The current plot number starts counting at 1 from the top-left then continues as though you were reading English from left to right, top to bottom. To get the bottom right plot from the Supermongo example I would use `ax = fig.add_subplot(2,2,4)`.

<br/>

Matplotlib has many ways to easily manipulate multipanel figures. Check out this [Demo of multiple subplots](http://matplotlib.org/examples/pylab_examples/subplots_demo.html).

+-------------+----------------------------+---------------------------------+
|     Task    |         Supermongo         |              Python             |
+=============+============================+=================================+
| Plot Bounds | ```supermongo              | ```python                       |
|             | limits xmin xmax ymin ymax | plt.axis((xmin,xmax,ymin,ymax)) |
|             |                            | # also set each independently   |
|             |                            | plt.xlim(xmin,xmax)             |
|             |                            | plt.ylim(ymin,ymax)             |
|             | ```                        | ```                             |
+-------------+----------------------------+---------------------------------+
| Add Plot    | ```supermongo              | ```python                       |
|             | box                        | ax = fig.add_subplot(111)       |
|             | ```                        | ```                             |
+-------------+----------------------------+---------------------------------+

### Saving plots to file ###

Saving in Supermongo requires setting up a state to put the plot into. The following example from [Annika Peter](http://www.astro.caltech.edu/~apeter/sm/basic.html) shows how to set up the device then save to file (the last `hardcopy` is critical, you can also use `dev x11` to close).

```supermongo
dev postencap my_first_plot.eps
ctype black
set x=0.0,10.0,1.0
set y=x**2
lim x y
box
con x y
ptype 10 3
points x y
xlabel x
ylabel y
hardcopy
```

Matplotlib does not require you to set anything up prior to building the items. Instead, you can just save out the state or figure with a command. The following example mimics the Supermongo example. 

```python
import matplotlib.pylab as plt
import numpy as np
x = np.arange(0.0,10.0,1.0)
y = x**2
fig,ax = plt.subplots()
ax.plot(x,y,marker='o')
ax.set_xlabel("x")
ax.set_ylabel("y")
fig.savefig("my_first_plot.ps")
```

__Note:__ Matplotlib is smart about it's saving methods. If you want to create a pdf not ps you just use the ".pdf" extension and it will save to that format. Many other formats are supported (e.g. png, pdf, jpg, gif, etc)

<br/>
<br/>
<br/>


# Could publish the programming section later # {style="font-size:40px;font-weight:bold"}

----------------------------------------------------

## Programming ##

Supermongo was developed to be plotting language. However, within it's syntax you can specify any programming task which makes it more or less a complete language. However, you should avoid using SuperMongo for more than plots as much as possible. Other programming languages have much better implementations allowing you to write your code faster, debug easier, and for it to run more efficiently. 

For example, Python is a complete language which has good implementations of many programming concepts. It's a language not just for plotting but 

### Reading in Data ###

### Syntax ###

### Programming Actions ###

define x 1 | x = 1

set x = {1,2,3} | x = [1,2,3]

set x = {1,2,3} | x = np.array([1,2,3])

set x = 0,10,1 | x = np.arange(0,10,1)
set x = 0,10,1 | x = list(range(0,10,1))



### Control Structures ###


__if statement__

+-----------------+-----------------+
|    Supermongo   |      Python     |
+=================+=================+
|```supermongo    |```python        |
|if (expr) {      |if expr:         |
|    echo True    |    print("True")|
|}                |                 |
|```              |```              |
+-----------------+-----------------+

__if,elseif,else statement__

```supermongo
if('Robert' == 'Patricia') {
   echo Something's wrong
} else { if('Patricia' == 'Ralph') {
   echo Still wrong
} else {
   echo Go Yankees
}}
```

```python
if 'Robert' == 'Patricia':
    print("Something's wrong")
elif 'Patricia' == 'Ralph':
    print("Still wrong")
else:
    print("Go Yankees")
```

+--------------+-----------------+-----------------+
|     Task     |    Supermongo   |      Python     |
+==============+=================+=================+
| Conditionals | ```supermongo   | ```python       |
|              | # same          | # same          |
|              | ==,!=,>,<,>=,<= | ==,!=,>,<,>=,<= |
|              | ```             | ```             |
+--------------+-----------------+-----------------+
| Logic        | ```supermongo   | ```python       |
|              | a && b          | a and b         |
|              | a  b            | a or b          |
|              | !a              | !a              |
|              | ```             | ```             |
+--------------+-----------------+-----------------+


## Shout Outs ##

Acknowledgments go to Robert Lupton and Patricia Monger for creating [SM](http://www.astro.princeton.edu/~rhl/sm/) which really was revolutionary for it's time. Special thanks to [Annika Peter](http://www.astro.caltech.edu/~apeter/sm/basic.html), [Craig Rudick](http://astroweb.astr.cwru.edu/craig/sm/plot_sm.html) and [Rebecca Stanek](http://www.rebeccastanek.com/super/) for their Supermongo guides. They helped me immensely when I learned Supermongo and in writing this guide.




