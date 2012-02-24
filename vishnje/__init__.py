import os
import sys
import logging
import webbrowser
import pkg_resources
from collections import namedtuple
from optparse import OptionParser

import cherrypy
from cherrypy.lib.static import serve_file

logging.basicConfig(level=logging.INFO)

Example = namedtuple('Example', 'path data')

def serve(example, data):

    path = example.path
    dir  = os.path.dirname(path)
    current_dir  = os.path.abspath(pkg_resources.resource_filename(__name__, '.'))

    def serve_data(): return data
    serve_data.exposed = True

    config = {
        # for d3.js
        '/d3' : {
            'tools.staticdir.on'  : True,
            'tools.staticdir.dir' : current_dir + '/d3',
        },
        dir : {
            'tools.staticdir.on'  : True,
            'tools.staticdir.dir' : current_dir + dir,
        }
    }

    cherrypy.tree.mount(root=None, config=config)
    cherrypy.tree.mount(serve_data, example.data, config=config)
    cherrypy.engine.start_with_callback(
        webbrowser.open,
        ('http://localhost:8080/{path}'.format(path=path),),
        )
    cherrypy.engine.block()

def read():
    usage = "usage: %prog [options] data_file"
    parser = OptionParser()
    (options, args) = parser.parse_args()
    if args:
        with open(args[0]) as f: return f.read()
    else:
        logging.info('Reading from standard input')
        return sys.stdin.read()

def present(example):
    serve(example, read())

available = ['Available visualizations:']

def parallel():
    present(Example(
        path='/d3/examples/parallel/parallel.html',
        data='/d3/examples/parallel/cars.csv',
        ))
available.append('parallel')

def splom():
    present(Example(
        path='/d3/examples/splom/splom.html',
        data='/d3/examples/splom/flowers.json',
        ))
available.append('splom')

def crimea_stacked_area():
    present(Example(
        path='/d3/examples/crimea/crimea-stacked-area.html',
        data='/d3/examples/crimea/crimea.csv',
        ))
available.append('crimea_stacked_area')

def zoom():
    present(Example(
        path='/d3/examples/zoom/zoom.html',
        data='/d3/examples/zoom/sp500.csv',
        ))
available.append('zoom')

def marimekko():
    present(Example(
        path='/d3/examples/marimekko/marimekko.html',
        data='/d3/examples/marimekko/marimekko.json',
        ))
available.append('marimekko')

def bar():
    present(Example(
        path='/d3/examples/bar/bar.html',
        data='/d3/examples/bar/sample-data.csv',
        ))
available.append('bar')

if __name__=='__main__':
    logging.info(format('\n\t'.join(available)))
