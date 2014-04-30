import os.path
import time
from multiprocessing import Process
import pkgutil
import unittest2 as unittest

from confeitaria import DynamicPage

import cherrypy
import requests

TEST_JS_CONTENT = pkgutil.get_data(__name__, 'js/test.js')
TEST_CSS_CONTENT = pkgutil.get_data(__name__, 'css/test.css')

class DynamicPageTestCase(unittest.TestCase):

    def test_retrieve_js(self):
        class TestPage(DynamicPage):
            pass
        
        self.assertEqual(TEST_JS_CONTENT, TestPage().js.index('test.js'))

    def test_retrieve_css(self):
        class TestPage(DynamicPage):
            pass

        self.assertEqual(TEST_CSS_CONTENT, TestPage().css.index('test.css'))


class DynamicPageHttpServerTestPage(unittest.TestCase):

    def test_provide_js_through_http(self):
        result = requests.get('http://localhost:8080/js/test.js')

        self.assertEqual(200, result.status_code)
        self.assertEqual(TEST_JS_CONTENT, result.text)

    def test_provide_js_through_http(self):
        result = requests.get('http://localhost:8080/css/test.css')

        self.assertEqual(200, result.status_code)
        self.assertTrue(result.headers['content-type'].startswith('text/css'))
        self.assertEqual(TEST_CSS_CONTENT, result.text)

    @classmethod
    def setUpClass(cls):
        class TestPage(DynamicPage):
            pass

        page = TestPage()
        cls.process = Process(target=page.run)
        cls.process.start()
        time.sleep(0.5)
    
    @classmethod
    def tearDownClass(cls):
        cls.process.terminate()
