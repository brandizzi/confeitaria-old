import os.path
import pkgutil
import cherrypy

from .page import Page

class DynamicPage(Page):

    @cherrypy.expose
    def js(self, path):
        path = os.path.join('js', path)
        return pkgutil.get_data(self.__class__.__module__, path)

    @cherrypy.expose
    def css(self, path):
        path = os.path.join('css', path)
        return pkgutil.get_data(self.__class__.__module__, path)
