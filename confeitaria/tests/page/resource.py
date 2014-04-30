import time
import pkgutil
import unittest2 as unittest
from multiprocessing import Process

from confeitaria import Page, ResourcePage

import cherrypy
import requests

class ResourcePageTestCase(unittest.TestCase):

    def test_serve_resource(self):
        txt_content = pkgutil.get_data(__name__, 'txt/test.txt')
        resource_page = ResourcePage(root=__name__, directory='txt')
        self.assertEqual(txt_content, resource_page.index('test.txt'))

    def test_use_parent_resouce(self):
        class TestPage(Page):
            pass

        page = TestPage()
        page.txt = ResourcePage(directory='txt')

        txt_content = pkgutil.get_data(__name__, 'txt/test.txt')

        self.assertEqual(txt_content, page.txt.index('test.txt'))

    def test_set_content_type(self):
        resource_page = ResourcePage(
            root=__name__, directory='css', content_type='text/css'
        )

        p = Process(target=resource_page.run)
        try:
            p.start()
            time.sleep(0.5)

            result = requests.get('http://localhost:8080/test.css')

            self.assertEqual(200, result.status_code)
            content_type = result.headers['content-type']
            self.assertTrue(content_type.startswith('text/css'))
        except AssertionError as e:
            raise
        except Exception as e:
            self.fail(e)
        finally:
            p.terminate()

    def test_404_not_found(self):
        resource_page = ResourcePage(
            root=__name__, directory='txt', content_type='text/plain'
        )

        p = Process(target=resource_page.run)
        try:
            p.start()
            time.sleep(0.5)

            result = requests.get('http://localhost:8080/no-such-file.txt')

            self.assertEqual(404, result.status_code)
        except AssertionError as e:
            raise
        except Exception as e:
            self.fail(e)
        finally:
            p.terminate()
