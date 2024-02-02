import unittest
import os
from utils import clone_project
from utils import delete_dir
from constant import path

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.url = 'https://github.com/tomoya0318/tomoya0318.git'
        self.root = path.ROOT

    def test_clone_project(self):
        clone_project(self.root, self.url)
        dir = f'{path.TMP}/origin'
        self.assertTrue(os.path.exists(dir), f'fail clone.')
        delete_dir(dir)