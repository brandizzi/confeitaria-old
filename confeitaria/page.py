import cherrypy

class Page(object):
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

