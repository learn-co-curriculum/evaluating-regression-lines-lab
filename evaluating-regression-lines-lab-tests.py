import unittest
from ipynb.fs.full.evaluatingRegressionLinesLab import (movies, y, error, regression_formula, squared_error, residual_sum_squares)

class TestDistance(unittest.TestCase):
    def test_regression_formula(self):
        self.assertEqual(regression_formula(100000), 270000.0)

    def test_y(self):
        self.assertEqual(y(13000000, movies), 25682380.0)

    def test_error(self):
        self.assertEqual(error(13000000, movies), 3482380.0)

    def test_squared_error(self):
        self.assertEqual(squared_error(movies[0]['budget'], movies), 12126970464400.0)

    def sum_squared_error(self):
        self.assertEqual(residual_sum_squares(movies), 3.0025171100327725e+17)

if __name__ == '__main__':
    unittest.main()
