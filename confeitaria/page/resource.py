import os.path
import pkgutil
import cherrypy

from .page import Page

class ResourcePage(Page):
    def __init__(self, root, directory, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.root = root
        self.directory = directory

    @cherrypy.expose
    def index(self, resource, *args, **kwargs):
        resource_path = os.path.join(self.directory, resource)

        return pkgutil.get_data(self.root, resource_path)
