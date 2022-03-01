import unittest
from solution import table_sum
from grid import Grid


class MyTestCase(unittest.TestCase):
    def test_range(self):
        for i in range(1, 17):
            for j in range(1, 17):
                for l in range(0, 2):
                    self.assertEqual(table_sum(i, j, l),
                                     Grid(i, j, l).sum(),
                                     f'input: ({i}, {j}, {l}) fails?')

    def test_zero(self):
        for l in range(0, 10):
            self.assertEqual(table_sum(0, 0, l), 0)


if __name__ == '__main__':
    unittest.main()
