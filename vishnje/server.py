# Based upon http://code.activestate.com/recipes/442481-creating-browser-based-desktop-apps-with-cherrypy-/

default_page = '''
<html>
<head>
<title>Vishnje visualization</title>
<script type="text/javascript"></script>
</head>
    <body>
        Body
    </body>
</html>
'''

def present(page=None):

    if not page: page = default_page

    import cherrypy
    class Root(object):
        def index(self):
            return page
        index.exposed = True

    import webbrowser
    cherrypy.tree.mount(Root(), '/')
    cherrypy.engine.start_with_callback(
        webbrowser.open,
        ('http://localhost:8080/',),
        )
    cherrypy.engine.block()

if __name__=='__main__':
    present()
