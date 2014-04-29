import time
import unittest2 as unittest
from multiprocessing import Process

from confeitaria import Page

import cherrypy
import requests

class PageTestCase(unittest.TestCase):

    def test_extend(self):
        class TestPage(Page):
            pass

        self.assertIsNotNone(TestPage().index())

    def test_provide_http_server(self):
        class TestPage(Page):
            @cherrypy.expose
            def index(self):
                return 'ok'

        page = TestPage()
        p = Process(target=page.run)
        try:
            p.start()
            time.sleep(0.5)

            result = requests.get('http://localhost:8080')

            self.assertEqual(200, result.status_code)
            self.assertEqual('ok', result.text)
        except Exception as e:
            self.fail(e)
        finally:
            p.terminate()

    def test_has_path(self):
        class TestPage(Page):
            @cherrypy.expose
            def index(self):
                return 'ok'

        self.assertEqual('/', TestPage().path)

    def test_path_defined_on_init(self):
        class TestPage(Page):
            @cherrypy.expose
            def index(self):
                return 'ok'

        self.assertEqual('/subdir/', TestPage(path='/subdir/').path)
