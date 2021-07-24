"""
Tests IO functions.
"""
import unittest
from os.path import join, isdir

from mlaid.utils.path import repo_path
from mlaid.utils.io import load_pkl, save_pkl


class TestPickle(unittest.TestCase):
    """Class to run tests on functions in utils/io.py"""

    @classmethod
    def setUpClass(cls):
        cls.assets_dir = join(repo_path, "assets")
        assert isdir(cls.assets_dir)

        cls.data = {"a": 1, "b": 2, "c": 3}
        cls.pkl_path = join(cls.assets_dir, "data.pkl")
    
    def test_save_pkl(self):
        save_pkl(self.data, self.pkl_path)
    
    def test_load_pkl(self):
        data = load_pkl(self.pkl_path)
        self.assertEqual(data, self.data)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestPickle('test_save_pkl'))
    suite.addTest(TestPickle('test_load_pkl'))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite())