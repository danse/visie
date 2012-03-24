
Vishnje is a plotting tool, and a d3.js_ playground for `python 3`_.

The purpose of the project is to leverage d3_ power for a desktop user which
can understand python and javascript, in order to visualize data from the
command line.

In order to use it, install it within your virtualenv with pip::

 $ virtualenv --python python3 ~/ENV
 $ source ~/ENV/bin/activate
 $ pip install git+git://github.com/danse/vishnje.git
 
Now you can use all the scripts, starting with ``vis-``, these scripts will
allow you to run d3_ examples upon your data files::

 $ cat > my_cars.csv
 name,economy (mpg),cylinders,displacement (cc),power (hp),weight (lb),0-60 mph (s),year
 AMC Ambassador Brougham,13,8,360,175,3821,11,73
 AMC Ambassador DPL,15,8,390,190,3850,8.5,70
 AMC Ambassador SST,17,8,304,150,3672,11.5,72
 AMC Concord DL 6,20.2,6,232,90,3265,18.2,79
 AMC Concord DL,18.1,6,258,120,3410,15.1,78
 AMC Concord DL,23,4,151,,3035,20.5,82
 $ vis-parallel my_cars.csv

This will launch the web server and start your browser on the right page,
trying to emulate a rough web-based desktop application (an idea taken by this
CherryPy recipe_). Type Ctrl-C on the launch shell in order to shutdown the
server.

The scripts can also read data from the command line (on my bash I have to type
Ctrl-D two times in order to close the stream). While it is difficult to use
this feature by hand due to the lack of data parsing controls, this can be
useful in order to feed the scripts pipelining them with data generators.

.. _recipe: http://code.activestate.com/recipes/442481-creating-browser-based-desktop-apps-with-cherrypy-/
.. _d3: http://mbostock.github.com/d3/
.. _d3.js: d3_
.. _python 3: http://mbostock.github.com/d3/
