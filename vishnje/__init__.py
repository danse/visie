import os
import sys
import logging
import webbrowser
from optparse import OptionParser
import json

import cherrypy

javascript_exit_handling = '''
<script type='text/javascript'>
    exit = function(e){{window.location='http://localhost:8080/stop';}}
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
        self.page         = page.format(exit=javascript_exit_handling)
        self.data_content = None

    def init_data(self, data):
        self.data_content = json.dumps(data)

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

class D3Application(Application):
    '''
    An application suitable for D3 scripts. It includes an empty body, D3
    library, and just requires the javascript

    >>> _=D3Application('')
    '''

    HTML='''<!DOCTYPE html>
<html>
  <head>
    <!--<meta http-equiv="cache-control" content="no-cache" />
    <meta http-equiv="pragma" content="no-cache" />
    <meta http-equiv="expires" content="0" />-->
    <title>{title}</title>
    {exit}
    <script type="text/javascript" src="http://d3js.org/d3.v2.min.js"></script>
    <style type="text/css">
    </style>
  </head>
  <body>
    <script type="text/javascript">
        {js}
    </script>
  </body>
</html>
'''

    def __init__(self, js, title='D3 visualization'):
        self.page = D3Application.HTML.format(
            title=title,
            js=js,
            exit=javascript_exit_handling)
        self.data_content = None

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
