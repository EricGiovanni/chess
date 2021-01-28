import unittest

from chess.hello import hello

class HelloTestCase(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), 'Hello world!')
