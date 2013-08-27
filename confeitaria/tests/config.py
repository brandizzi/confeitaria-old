import unittest2 as unittest

import confeitaria.config as config

class ConfigTestCase(unittest.TestCase):

    def test_set_get(self):
        config.set('test', 'my test value')
        self.assertEqual(config.get('test'), 'my test value')

    def test_get_none(self):
        self.assertEqual(config.get('test'), None)

    def test_clear(self):
        config.set('test', 'my test value')
        self.assertEqual(config.get('test'), 'my test value')
        config.clear()
        self.assertEqual(config.get('test'), None)
    
    def setUp(self):
        config.clear()
