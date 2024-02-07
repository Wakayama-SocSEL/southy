import os
import unittest

from southy import constant, LocalRepository


class TestCollect(unittest.TestCase):
    def setUp(self):
        self.url = 'https://github.com/tomoya0318/tomoya0318.git'


    def test_init(self):
        LocalRepository(self.url)
        self.assertTrue(len(os.listdir(constant.path.REPO_CACHE)) > 0, 'fail clone.')


    def test_findall_commit_hashes(self):
        repo = LocalRepository(self.url)
        self.assertIsInstance(repo.findall_commit_hashes(), list)


    def test_findall_commit_diffs(self):
        repo = LocalRepository(self.url)
        self.assertIsInstance(repo.findall_commit_diffs(), list)
