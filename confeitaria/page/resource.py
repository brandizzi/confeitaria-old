import os.path
import pkgutil
import cherrypy

from .page import Page

class ResourcePage(Page):

    def __init__(self, directory, content_type='text/plain', root=None,
            *args, **kwargs):

        Page.__init__(self, *args, **kwargs)

        self._root = root
        self.directory = directory
        self.content_type = content_type

    @cherrypy.expose
    def index(self, resource, *args, **kwargs):
        cherrypy.response.headers['Content-Type']= self.content_type

        resource_path = os.path.join(self.directory, resource)

        try:
            return pkgutil.get_data(self.root, resource_path)
        except IOError as e:
            raise cherrypy.HTTPError(404)

    @property
    def root(self):
        if self._root is not None:
            return self._root
        elif self.parent is not None:
            return self.parent.__class__.__module__
        else:
            return self.__class__.__module__
