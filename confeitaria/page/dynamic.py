import os.path
import pkgutil
import cherrypy

from .page import Page
from .resource import ResourcePage

class DynamicPage(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.js = ResourcePage(
            directory='js', content_type='application/javascript'
        )
        self.css = ResourcePage(directory='css', content_type='text/css')
