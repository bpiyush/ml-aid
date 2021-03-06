"""
Tests pythonic operations functions.
"""
import unittest
from os.path import join, isdir
import numpy as np
import torch

from mlaid.utils.path import repo_path
from mlaid.utils.ops import DotDict, get_from_dict, set_in_dict, tensorize, numpify
from mlaid.utils.log import color, print_update


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
    
    def test_tensorize(self):
        x = np.ones((3, 4, 5))
        x_ = tensorize(x)
        self.assertTrue((torch.ones((3, 4, 5)) == x_).all())

    def test_numpify(self):
        # vanilla case
        x = torch.ones((3, 4, 5))
        x_ = numpify(x)
        self.assertTrue((np.ones((3, 4, 5)) == x_).all())

        # case when x is differentiable
        x = torch.ones((3, 4, 5), requires_grad=True)
        x_ = numpify(x)
        self.assertTrue((np.ones((3, 4, 5)) == x_).all())
    
    def test_dotdict(self):
        x = DotDict(self._dict)
        self.assertEqual(x.a.b.c, 10)
        self.assertEqual(x.x, 3)
    
    def test_print_update(self):
        print_update("Sample update message")
    
    def test_color(self):
        print(color("Sample colored message", "yellow"))


def suite():
    """Helper function to run tests in desired order and grouping.
    """
    suite = unittest.TestSuite()
    suite.addTest(TestOps('test_get_from_dict'))
    suite.addTest(TestOps('test_set_in_dict'))
    suite.addTest(TestOps('test_tensorize'))
    suite.addTest(TestOps('test_numpify'))
    suite.addTest(TestOps('test_dotdict'))
    suite.addTest(TestOps('test_print_update'))
    suite.addTest(TestOps('test_color'))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite())

