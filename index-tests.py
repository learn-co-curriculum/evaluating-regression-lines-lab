import unittest
from ipynb.fs.full.index import (x_values, y_values, y_actual, error, error_line_trace, error_line_traces, regression_formula,
 squared_error, residual_sum_squares, trace_rss, titles)

class TestError(unittest.TestCase):
    def test_x_values(self):
        self.assertEqual(len(x_values), 30)
        self.assertEqual(x_values[0], 13000000)

    def test_y_values(self):
        self.assertEqual(len(y_values), 30)
        self.assertEqual(y_values[0], 25682380.0)

    def test_titles(self):
        self.assertEqual(len(titles), 30)
        self.assertEqual(titles[0], '21 &amp; Over')

    def test_regression_formula(self):
        self.assertEqual(regression_formula(100000), 270000.0)
        self.assertEqual(regression_formula(250000), 525000.0)

    def test_y_actual(self):
        self.assertEqual(y_actual(13000000, x_values, y_values), 25682380.0)

    def test_error(self):
        self.assertEqual(error(x_values, y_values, 1.7, 100000, 13000000), 3482380.0)

    def test_error_line_trace(self):
        error_line_trace0 = error_line_trace(x_values, y_values, 1.7, 10000, 120000000)
        self.assertEqual(error_line_trace0['mode'], 'line')
        self.assertEqual(error_line_trace0['x'], [120000000, 120000000])
        self.assertEqual(error_line_trace0['y'], [93050117.0, 204010000.0])
        self.assertEqual(error_line_trace0['name'], 'error at 120000000')


    def test_error_line_traces(self):
        traces = error_line_traces(x_values[0:5], y_values[0:5], 1.7, 100000)
        self.assertEqual(len(traces), 5)
        self.assertEqual(traces[-1]['mode'], 'line')
        self.assertEqual(traces[-1]['name'], 'error at 40000000')
        self.assertEqual(traces[-1]['x'], [40000000, 40000000])
        self.assertEqual(traces[-1]['y'], [95020213.0, 68100000.0])

    def test_squared_error(self):
        self.assertEqual(squared_error(x_values, y_values, 1.7, 100000, 13000000), 12126970464400.0)

    def test_rss(self):
        self.assertEqual(residual_sum_squares(x_values, y_values, 1.7, 100000), 3.0025171100327725e+17)

    def test_trace_rss_value(self):
        self.assertEqual(trace_rss(x_values, y_values, 1.7, 100000), {'type': 'bar', 'x': ['RSS'], 'y': [3.0025171100327725e+17]})
