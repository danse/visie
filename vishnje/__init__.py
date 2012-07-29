import os
import sys
import logging
import webbrowser
from optparse import OptionParser

import cherrypy

javascript_exit_handling = "window.onbeforeunload=function(e){window.location='http://localhost:8080/stop';}"

class Application:

    def __init__(page):
        self.page = page
        self.data = None

    def init_data(data, path='/data'):
        self.data      = data
        self.data_path = path

    def root(self):
        return self.page
    root.exposed = True

    def serve_data(self):
        return self.data
    root.exposed = True

    @staticmethod
    def stop():
        exit()
    stop.exposed = True

    def launch(self):
        cherrypy.tree.mount(self.root, '/')
        cherrypy.tree.mount(self.stop, '/stop')
        if self.data:
            cherrypy.tree.mount(self.serve_data, self.data_path)
        cherrypy.engine.start_with_callback(
            webbrowser.open,
            ('http://localhost:8080/',),
            )
        cherrypy.engine.block()

def find_stream(args=None):
    if args:
        with open(args[0]) as f:
            return f
    else:
        logging.info('Reading from standard input')
        return sys.stdin

def main():
    usage = "usage: %prog [options] file.html"
    (options, args) = OptionParser().parse_args()
    stream = find_stream(args)
    page   = stream.read()
    Application(page).launch()

if __name__=='__main__': main()
