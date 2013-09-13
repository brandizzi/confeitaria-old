import unittest2 as unittest

from confeitaria import Page

import cherrypy

class PageTestCase(unittest.TestCase):

    def test_extend(self):
        class TestPage(Page):
            @cherrypy.expose
            def index(self):
                return 'ok'

        self.assertEqual('ok', TestPage().index())
