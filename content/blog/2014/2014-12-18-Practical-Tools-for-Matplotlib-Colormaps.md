title: Practical Tools for Matplotlib Colormaps
date: Thu Dec 18 09:28:50 2014
template: article
authors: Dylan Gregersen
status: published
comments: true
css: static/css/blog/practical-tools-for-mpl.css
category: Programming
tags: plotting, programming, python, matplotlib, colormaps
summary: Choosing a good colormap is hard. Jet always looks pretty but just try printing in black & white and everything you thought you knew about your data changes.
+
I have several resources I use when picking a good colormap. Click the Read more to find out more.

# Color Maps Rock! #

I like colorful plots. They may cost [alot](http://hyperboleandahalf.blogspot.com/2010/04/alot-is-better-than-you-at-everything.html) to publish in a research journal but they're just so pretty. Quite a few blogs have been written ranting about rainbow colormaps and also about how to choose really good colormaps. 

This blog is devoted to practical tools I use to help me with colormapping. The actual code is in a github gist of [Matplotlib Colormap Tools](https://gist.github.com/astrodsg/09bfac1b68748967ed8b#file-mpl_colormap_tools)


<br/>
<br/>


Some other useful colormap links

* [Maplotlib: Choosing Colormaps](http://matplotlib.org/users/colormaps.html)
* [Jake Vanderplas: How bad is your colormap](https://jakevdp.github.io/blog/2014/10/16/how-bad-is-your-colormap/)
* [Custom Colormap Generator](http://colormap.org/)

For general color layouts:

* [Colorbrewer](http://colorbrewer2.org/)
* [Paletton](http://paletton.com/#uid=1000u0kllllaFw0g0qFqFg0w0aF) - a really cool color scheme tool which includes tools to filter by colorblindness

<br/>
<br/>
<br/>


Below is a really cool colormap image of the Milky Way's magnetic field [captured by the Planck spacecraft](http://public.planck.fr/resultats/249-planck-revele-l-invisible)

<img src="/static/img/blog/Plank-Galactic-Magentic-Field-640x640.jpg" alt="Plank Galactic Magnetic Field" style="height: 100%; width: 100%; max-height:500px; "></img>



## Colormap Reference ##

Several colormap references scripts/functions exist; mine is better (haha). In my [Matplotlib Colormap Tools](https://gist.github.com/astrodsg/09bfac1b68748967ed8b#file-mpl_colormap_tools) file I have a function called `show_mpl_cmaps`. This uses a lookup table to group together relevant colormaps and a graifier to also show what that colormap looks like in gray scale. I've added this to my PYTHONSTARTUP script so when I need a quick reference I can just open a terminal and type `show_mpl_cmaps()` to get:

![Matplotlib Colormaps](/static/img/blog/mpl_colormaps.png){}


## Truncating Colormaps ## 

Search Keywords: Reducing color range, shorten colormap, remove white from colormap

I searched for a while and could find something that made a colormap cut off certain colors. For example, taking the `plt.cm.rainbow` and reducing it to only blue to orange (I know rainbow is terrible, but humor me). Or you want to use `plt.cm.gist_heat` but cut off the white top. 

I hope if you're reading this I can save you some time in having already worked out a good way to truncate a colormap. It's a pretty short function I called `truncate_cmap` which I've included in [Matplotlib Colormap Tools](https://gist.github.com/astrodsg/09bfac1b68748967ed8b#file-mpl_colormap_tools) gist.

<div class="row mpl-cmap">
<div class="span6">
<div class="cmap-image-header"><p>plt.colormap(plt.imshow(cnts,cmap=plt.cm.rainbow))</p>
</div>
<img src="/static/img/blog/cmap_rainbow.svg" alt="Colormap"></img>
</div>
<div class="span6">
<div class="cmap-image-header"><p>plt.colormap(plt.imshow(cnts,cmap=truncate_cmap(plt.cm.rainbow,n_min=40,n_max=210))</p>
</div>
<img src="/static/img/blog/cmap_rainbow_truncated.svg" alt="Truncated Colormap"></img>
</div>
</div>


## The MonoColorMap ##

The final tool I'll leave you with is my own...`MonoColormap`. It's a silly colormap which always returns the same color (hence mono-color). You instantiate it `cmap=MonoColormap('r')` and can use any maplotlib color or hex color. I found it useful when I wanted to overplot some image but just have it gray out with some opacity. It's also located in [Matplotlib Colormap Tools](https://gist.github.com/astrodsg/09bfac1b68748967ed8b#file-mpl_colormap_tools) gist. 

## In Conclusion... ##

Hope this helps you with colormaps. If you didn't figure out from the post, all the functions and code are publicly available as a github gist at [Matplotlib Colormap Tools](https://gist.github.com/astrodsg/09bfac1b68748967ed8b#file-mpl_colormap_tools) 




