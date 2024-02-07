import os
import unittest

from southy import constant
from southy.utils import workspace


class TestUtils(unittest.TestCase):
    def test_create_tmp_dir(self):
        self.assertTrue(os.path.isdir(workspace.create_tmp_dir()), 'fail mkdir.')
