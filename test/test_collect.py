import unittest
from collect import GetHash
from collect import get_diff
from constant import path

class TestCollect(unittest.TestCase):
    def setUp(self):
        self.root = path.ROOT
        self.url = 'https://github.com/tomoya0318/tomoya0318.git'

    def test_GetHash(self):
        gh = GetHash()
        result = gh.get_hash(self.root)
        self.assertIsInstance(result, list)
    
    def test_diff(self):
        get_diff(path.ROOT, self.url)
