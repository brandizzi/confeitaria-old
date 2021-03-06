import cherrypy

class Page(object):
    def __init__(self, path='/'):
        self.exposed = True
        self.path = path
        self.parent = None

    @cherrypy.expose
    def index(self, *args, **kwargs):
        return '''<!doctype html>
        <html>
            <head>
                <title>Confeitaria's simplest page</title>
            </head>
            <body>
                <p><code>Page</code> is Confeitaria's simplest page</code></p>
            </body>
        </html>'''

    def run(self, config=None):
        if config == None:
            config = {
                'global': {
                    'log.screen': False,
                    'log.access_file': '/tmp/confeitaria.assess.log',
                    'log.error_file': '/tmp/confeitaria.assess.log'
                }
            }
        cherrypy.quickstart(self, config=config)

    def __setattr__(self, attribute_name, value):
        if isinstance(value, Page) and attribute_name != 'parent':
            value.path = self.path + attribute_name + '/'
            value.parent = self
        object.__setattr__(self, attribute_name, value)

    def __call__(self, *args, **kwargs):
        page = self

        try:
            attr = getattr(self, args[0])
            if isinstance(attr, Page):
                page = getattr(self, args[0])
        except Exception as e:
            page = self

        return page.index(*args, **kwargs)
