import os
import cherrypy
import webbrowser
from cherrypy.lib.static import serve_file

from collections import namedtuple

Example = namedtuple('Example', 'path data')

pwd = "/home/francesco/repos/vishnje/vishnje/"
parallel = Example(
    path='d3/examples/parallel/parallel.html',
    data='d3/examples/parallel/cars.csv',
    )
test = Example(
    path='d3/',
    data='data',
    )

def process(file):

    example = parallel
    path = example.path
   #assert os.path.exists(path)
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

if __name__=='__main__':
    import sys
    with open(sys.argv[1]) as f: file = f.read()
    process(file)
