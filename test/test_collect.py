import unittest
from collect import GetHash
from constant import path

class TestCollect(unittest.TestCase):
    def setUp(self):
        self.root = path.ROOT

    def test_GetHash(self):
        gh = GetHash()
        result = gh.get_hash(self.root)
        self.assertIsInstance(result, list)
