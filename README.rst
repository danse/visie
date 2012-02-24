
Vishnje is a plotting tool, and a d3.js_ playground for `python 3`_.

The purpose of the project is to leverage d3_ power for a desktop user which
can understand python and javascript, in order to visualize data quickly.

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

The project is based upon CherryPy, in order to run a rough web-based desktop
application.

.. _d3: http://mbostock.github.com/d3/
.. _d3.js: d3_
.. _python 3: http://mbostock.github.com/d3/
