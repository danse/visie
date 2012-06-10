import os
import sys
import logging
import webbrowser
from optparse import OptionParser

import cherrypy

javascript_exit_handling = "window.onbeforeunload=function(e){window.location='http://localhost:8080/stop';}"

def launch(page):

    def root(): return page
    root.exposed = True
    def stop(): exit()
    stop.exposed = True

    cherrypy.tree.mount(root, '/')
    cherrypy.tree.mount(stop, '/stop')
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
    launch(page)

if __name__=='__main__': main()
