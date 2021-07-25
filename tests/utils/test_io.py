"""
Tests IO functions.
"""
import unittest
from os.path import join, isdir

from mlaid.utils.path import repo_path
from mlaid.utils.io import (
    load_pkl, save_pkl, load_yml, save_yml, load_json, save_json, load_txt, save_txt
)


class TestPickle(unittest.TestCase):
    """Class to run tests on `pickle` functions in utils/io.py"""

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


class TestYAML(unittest.TestCase):
    """Class to run tests on `yaml` functions in utils/io.py"""

    @classmethod
    def setUpClass(cls):
        cls.assets_dir = join(repo_path, "assets")
        assert isdir(cls.assets_dir)

        cls.data = {"a": 1, "b": 2, "c": 3}
        cls.yml_path = join(cls.assets_dir, "data.yml")
    
    def test_save_yml(self):
        save_yml(self.data, self.yml_path)
    
    def test_load_yml(self):
        data = load_yml(self.yml_path)
        self.assertEqual(data, self.data)


class TestJSON(unittest.TestCase):
    """Class to run tests on `json` functions in utils/io.py"""

    @classmethod
    def setUpClass(cls):
        cls.assets_dir = join(repo_path, "assets")
        assert isdir(cls.assets_dir)

        cls.data = {"a": 1, "b": 2, "c": 3}
        cls.json_path = join(cls.assets_dir, "data.json")
    
    def test_save_json(self):
        save_json(self.data, self.json_path)
    
    def test_load_json(self):
        data = load_json(self.json_path)
        self.assertEqual(data, self.data)


class TestTxt(unittest.TestCase):
    """Class to run tests on `txt` functions in utils/io.py"""

    @classmethod
    def setUpClass(cls):
        cls.assets_dir = join(repo_path, "assets")
        assert isdir(cls.assets_dir)

        cls.data = ["a", "b", "c"]
        cls.txt_path = join(cls.assets_dir, "data.txt")
    
    def test_save_txt(self):
        save_txt(self.data, self.txt_path)
    
    def test_load_txt(self):
        data = load_txt(self.txt_path)
        self.assertEqual(data, self.data)


def suite():
    """Helper function to run tests in desired order and grouping.
    """
    suite = unittest.TestSuite()
    suite.addTest(TestPickle('test_save_pkl'))
    suite.addTest(TestPickle('test_load_pkl'))
    suite.addTest(TestYAML('test_save_yml'))
    suite.addTest(TestYAML('test_load_yml'))
    suite.addTest(TestJSON('test_save_json'))
    suite.addTest(TestJSON('test_load_json'))
    suite.addTest(TestTxt('test_save_txt'))
    suite.addTest(TestTxt('test_load_txt'))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite())