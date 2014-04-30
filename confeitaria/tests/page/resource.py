import time
import pkgutil
import unittest2 as unittest
from multiprocessing import Process

from confeitaria import ResourcePage

import cherrypy
import requests

class ResourcePageTestCase(unittest.TestCase):

    def test_serve_resource(self):
        txt_content = pkgutil.get_data(__name__, 'txt/test.txt')
        resource_page = ResourcePage(root=__name__, directory='txt')
        self.assertEqual(txt_content, resource_page.index('test.txt'))

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
