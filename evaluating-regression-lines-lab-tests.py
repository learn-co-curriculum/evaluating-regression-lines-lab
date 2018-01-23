import unittest
from ipynb.fs.full.evaluatingRegressionLinesLab import (movies, y, error, squared_error,
 squared_errors, average_squared_error, root_mean_squared_error)

class TestDistance(unittest.TestCase):
    def test_y(self):
        self.assertEqual(y(13000000, movies), 25682380.0)

    def test_error(self):
        self.assertEqual(error(13000000, movies), 3482380.0)

    def test_squared_error(self):
        self.assertEqual(squared_error(movies[0]['budget'], movies), 12126970464400.0)

    def test_average_squared_error(self):
        self.assertEqual(average_squared_error(movies), 1.0008390366775908e+16)

    def test_root_mean_squared_error(self):
        self.assertEqual(root_mean_squared_error(movies), 100041943.03778745)

if __name__ == '__main__':
    unittest.main()
