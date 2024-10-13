import unittest
from main import *

class Test(unittest.TestCase):
    def test_one_by_one(self):
        matrix = [[46]]
        result = row_sum(matrix)
        self.assertEqual(result, [46])

    def test_three_by_three(self):
        matrix = [
            [10, 10, 10],
            [21, 32, 43],
            [15, 25, 35],
        ]
        result = row_sum(matrix)
        self.assertEqual(result, [30, 96, 75])

    def test_six_by_three(self):
        matrix = [
            [10, 10, 10, 15, 25, 35],
            [21, 32, 43, 21, 32, 43],
            [15, 25, 35, 21, 32, 43],
        ]
        result = row_sum(matrix)
        self.assertEqual(result, [105, 192, 171])

    def test_awkward_six_rows(self):
        matrix = [
            [10, 10, 10],
            [15, 25, 35],
            [21],
            [21, 32, 43],
            [15, 25, 35, 21, 32, 43],
            [10, 10, 10, 15, 25, 35, 21, 32, 43],
        ]
        res = row_sum(matrix)
        self.assertEqual(res, [30, 75, 21, 96, 171, 201])

if __name__ == '__main__':
    unittest.main()
