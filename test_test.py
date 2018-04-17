import unittest
from ipynb.fs.full.index import (x_values, y_values, y_actual, error, error_line_trace, error_line_traces, regression_formula,
 squared_error, residual_sum_squares, trace_rmse, titles)

class TestError(unittest.TestCase):
    def test_x_values(self):
        self.assertEqual(len(x_values), 30)
        self.assertEqual(x_values[0], 13.0)

    def test_y_values(self):
        self.assertEqual(len(y_values), 30)
        self.assertEqual(y_values[0], 26.0)

    def test_titles(self):
        self.assertEqual(len(titles), 30)
        self.assertEqual(titles[0], '21 &amp; Over')

    def test_regression_formula(self):
        self.assertEqual(regression_formula(100), 180.0)
        self.assertEqual(regression_formula(250), 435.0)

    def test_y_actual(self):
        self.assertEqual(y_actual(13, x_values, y_values), 26.0)

    def test_error(self):
        self.assertEqual(error(x_values, y_values, 1.7, 10, 13), -6.099999999999994)

    def test_error_line_trace(self):
        error_line_trace0 = error_line_trace(x_values, y_values, 1.7, 10, 120)
        self.assertEqual(error_line_trace0['mode'], 'line')
        self.assertEqual(error_line_trace0['x'], [120, 120])
        self.assertEqual(error_line_trace0['y'], [93.0, 214.0])
        self.assertEqual(error_line_trace0['name'], 'error at 120')


    def test_error_line_traces(self):
        traces = error_line_traces(x_values, y_values, 1.7, 10)
        self.assertEqual(len(traces), 30)
        self.assertEqual(traces[-1]['mode'], 'line')
        self.assertEqual(traces[-1]['name'], 'error at 30.0')
        self.assertEqual(traces[-1]['x'], [30.0, 30.0])
        self.assertEqual(traces[-1]['y'], [35.0, 61.0])

    def test_squared_error(self):
        self.assertEqual(squared_error(x_values, y_values, 1.7, 10, x_values[0]), 37.20999999999993)

    def test_rss(self):
        self.assertEqual(residual_sum_squares(x_values, y_values, 1.7, 10), 320407.43000000005)

    def test_trace_rsme_value(self):
        regression_lines = [(1.7, 10), (1.9, 20)]
        self.assertEqual(trace_rmse(x_values, y_values, regression_lines), {'type': 'bar', 'x': ['m: 1.7 b: 10', 'm: 1.9 b: 20'], 'y': [19.0, 22.0]})
