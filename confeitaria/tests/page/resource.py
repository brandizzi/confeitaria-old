import time
import pkgutil
import unittest2 as unittest

from confeitaria import ResourcePage

import cherrypy
import requests

class ResourcePageTestCase(unittest.TestCase):

    def test_serve_resource(self):
        txt_content = pkgutil.get_data(__name__, 'txt/test.txt')
        resource_page = ResourcePage(root=__name__, directory='txt')
        self.assertEqual(txt_content, resource_page.index('test.txt'))