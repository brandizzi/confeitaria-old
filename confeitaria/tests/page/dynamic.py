import time
import unittest2 as unittest
from multiprocessing import Process
import pkgutil

from confeitaria import DynamicPage

import cherrypy
import requests

TEST_JS_CONTENT = pkgutil.get_data(__name__, 'js/test.js')

class DynamicPageTestCase(unittest.TestCase):

    def test_retrieve_js(self):
        class TestPage(DynamicPage):
            pass
        
        self.assertEqual(TEST_JS_CONTENT, TestPage().js('test.js'))

    def test_provide_js_through_http(self):
        class TestPage(DynamicPage):
            pass

        page = TestPage()
        p = Process(target=page.run)
        try:
            p.start()
            time.sleep(0.5)

            result = requests.get('http://localhost:8080/js/test.js')

            self.assertEqual(200, result.status_code)
            self.assertEqual(TEST_JS_CONTENT, result.text)
        except Exception as e:
            self.fail(e)
        finally:
            p.terminate()
