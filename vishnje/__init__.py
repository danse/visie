import os
import sys
import logging
import webbrowser
from optparse import OptionParser
import json

import cherrypy

javascript_exit_handling = '''
<script type='text/javascript'>
    exit = function(e){window.location='http://localhost:8080/stop';}
    window.onbeforeunload = exit
</script>
'''

class Application:
    '''
    >>> application = Application('This should be HTML...')
    >>> application.init_data(['this', 'will', 'become', 'json'])
    >>> application.launch() # doctest: +SKIP
    '''

    def __init__(self, page):
        self.page = page.format(exit=javascript_exit_handling)
        self.data = None

    def init_data(self, data, path='/data'):
        self.data_content = json.dumps(data)
        self.data_path    = path

    def index(self):
        return self.page
    index.exposed = True

    def data(self):
        return self.data_content
    data.exposed = True

    def stop(self):
        exit()
    stop.exposed = True

    def launch(self):
        cherrypy.tree.mount(self, '/')
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

def main(page=None):
    usage = "usage: %prog [options] file.html"
    (options, args) = OptionParser().parse_args()
    if not page:
        stream = find_stream(args)
        page   = stream.read()
    Application(page).launch()

if __name__=='__main__':
    main()
