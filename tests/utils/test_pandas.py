"""
Tests `pandas` functions.
"""
import unittest
from os.path import join, isdir
import pandas as pd

from mlaid.utils.path import repo_path
from mlaid.utils.pandas import apply_filters, apply_antifilters


class TestPandas(unittest.TestCase):
    """Test cases for pandas util functions"""

    @classmethod
    def setUpClass(cls) -> None:
        df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv")
        df = df.replace('[" ]','', regex=True)
        df.columns = [x.strip().replace('"', "") for x in df.columns]
        cls.df = df
    
    def test_apply_filters(self):
        _df = apply_filters(self.df, {"City": "Watertown"})
        self.assertEqual(_df.shape, (2, 10))

    def test_apply_antifilters(self):
        _df = apply_antifilters(self.df, {"City": "Watertown"})
        self.assertEqual(_df.shape, (126, 10))


def suite():
    """Helper function to run tests in desired order and grouping.
    """
    suite = unittest.TestSuite()
    suite.addTest(TestPandas('test_apply_filters'))
    suite.addTest(TestPandas('test_apply_antifilters'))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite())

