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
            pass

        self.assertEqual('/', TestPage().path)

    def test_path_defined_on_init(self):
        class TestPage(Page):
            pass

        self.assertEqual('/subdir/', TestPage(path='/subdir/').path)

    def test_append_parent_node_path(self):
        class RootPage(Page):
            pass
        class LeafPage(Page):
           pass

        root = RootPage(path='/root/')
        root.leaf = LeafPage()

        self.assertEqual('/root/leaf/', root.leaf.path)

    def test_get_child_page_content_through_http(self):
        class RootPage(Page):
            @cherrypy.expose
            def index(self):
                return 'root'
        class LeafPage(Page):
            @cherrypy.expose
            def index(self):
                return 'leaf'

        root = RootPage()
        root.leaf = LeafPage()

        p = Process(target=root.run)
        try:
            p.start()
            time.sleep(0.5)

            result = requests.get('http://localhost:8080')

            self.assertEqual(200, result.status_code)
            self.assertEqual('root', result.text)

            result = requests.get('http://localhost:8080/leaf')

            self.assertEqual(200, result.status_code)
            self.assertEqual('leaf', result.text)
        except AssertionError:
            raise
        except Exception as e:
            self.fail(e)
        finally:
            p.terminate()

    def test_is_callable(self):
        class TestPage(Page):
            @cherrypy.expose
            def index(self):
                return 'ok'

        page = TestPage()
 
        self.assertIsNotNone(page(), page.index())

    def test_is_exposed(self):
        class TestPage(Page):
            pass
 
        self.assertTrue(TestPage().exposed)

    def test_none_parent(self):
        page = Page(path='/root/')
        self.assertIsNone(page.parent)

    def test_set_parent(self):
        class RootPage(Page):
            pass
        class LeafPage(Page):
           pass

        root = RootPage(path='/root/')
        leaf = LeafPage()
        root.leaf = leaf

        self.assertEqual(root, leaf.parent)
