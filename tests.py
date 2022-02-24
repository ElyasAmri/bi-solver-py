import unittest
from solution import table_sum_noprint


class MyTestCase(unittest.TestCase):
    def test_range(self):
        for i in range(1, 17):
            for j in range(1, 17):
                self.assertTrue(table_sum_noprint(i, j, 0), f'input: ({i}, {j}, {0}) fails?')
                self.assertTrue(table_sum_noprint(i, j, 1), f'input: ({i}, {j}, {1}) fails?')


if __name__ == '__main__':
    unittest.main()
