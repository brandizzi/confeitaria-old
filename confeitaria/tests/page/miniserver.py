# A small server for interactive tests and personal satisfaction :)
import pkgutil
import cherrypy


from confeitaria import DynamicPage

HTML_DOCUMENT = pkgutil.get_data(__name__, 'index.html')

class TestPage(DynamicPage):

    @cherrypy.expose
    def index(self, *args, **kwargs):
        document = HTML_DOCUMENT.replace('{args}', repr(args))
        document = document.replace('{kwargs}', repr(kwargs))
        return document

if __name__ == "__main__":
    TestPage().run()
