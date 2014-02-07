import time
import unittest2 as unittest
from multiprocessing import Process
import pkgutil

from confeitaria import DynamicPage

import cherrypy
import requests

class DynamicPageTestCase(unittest.TestCase):

    def test_js_content(self):
        class TestPage(DynamicPage):
            pass
        
        self.assertEqual(pkgutil.get_data(__name__, 'js/test.js'), TestPage().js('test.js'))

    """def test_provide_http_server(self):
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
            """

