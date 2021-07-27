"""
Tests pythonic operations functions.
"""
import unittest
from os.path import join, isdir

from mlaid.utils.path import repo_path
from mlaid.utils.ops import get_from_dict, set_in_dict


class TestOps(unittest.TestCase):
    """Test cases for ops util functions"""

    @classmethod
    def setUpClass(cls) -> None:
        cls._dict = {"a": {"b": {"c": 2}}, "x": 3}
    
    def test_get_from_dict(self):
        value = get_from_dict(self._dict, ["a", "b", "c"])
        self.assertEqual(value, 2)

    def test_set_in_dict(self):
        set_in_dict(self._dict, ["a", "b", "c"], value=10)
        value = get_from_dict(self._dict, ["a", "b", "c"])
        self.assertEqual(value, 10)


def suite():
    """Helper function to run tests in desired order and grouping.
    """
    suite = unittest.TestSuite()
    suite.addTest(TestOps('test_get_from_dict'))
    suite.addTest(TestOps('test_set_in_dict'))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite())

