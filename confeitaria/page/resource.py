import os.path
import pkgutil
import cherrypy

from .page import Page

class ResourcePage(Page):

    def __init__(self, root, directory, content_type='text/plain',
            *args, **kwargs):

        Page.__init__(self, *args, **kwargs)

        self.root = root
        self.directory = directory
        self.content_type = content_type

    @cherrypy.expose
    def index(self, resource, *args, **kwargs):
        cherrypy.response.headers['Content-Type']= self.content_type

        resource_path = os.path.join(self.directory, resource)

        return pkgutil.get_data(self.root, resource_path)
