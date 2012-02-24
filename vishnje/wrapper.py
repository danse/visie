import os
import sys
import logging
import webbrowser
from collections import namedtuple

import cherrypy
from cherrypy.lib.static import serve_file

Example = namedtuple('Example', 'path data')

def process(file, example):

    pwd = "/home/francesco/repos/vishnje/vishnje/"

    path = example.path
    assert os.path.exists(path)
    data = example.data
    dir  = os.path.dirname(path)

    def serve_data(): return file
    serve_data.exposed = True

    config = {
        '/d3' : {
            'tools.staticdir.on'  : True,
            'tools.staticdir.dir' : pwd+'/d3',
        },
        '/d3/examples/parallel' : {
            'tools.staticdir.on'  : True,
            'tools.staticdir.dir' : pwd+dir,
        }
    }

    cherrypy.tree.mount(root=None, config=config)
    cherrypy.tree.mount(serve_data, '/'+data, config=config)
    cherrypy.engine.start_with_callback(
        webbrowser.open,
        ('http://localhost:8080/{path}'.format(path=path),),
        )
    cherrypy.engine.block()

def read():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f: return f.read()
    else:
        logging.info('Reading from standard input')
        return sys.stdin.read()

def present(example):
    file = read()
    process(file, example)

def parallel():
    present(Example(
        path='d3/examples/parallel/parallel.html',
        data='d3/examples/parallel/cars.csv',
        ))

if __name__=='__main__': parallel()
