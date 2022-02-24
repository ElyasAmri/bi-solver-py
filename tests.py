import unittest
from solution import table_sum_noprint
from grid import Grid


class MyTestCase(unittest.TestCase):
    def test_range(self):
        for i in range(1, 17):
            for j in range(1, 17):
                for l in range(0, 2):
                    self.assertEqual(table_sum_noprint(i, j, l),
                                     Grid(i, j, l).sum(),
                                     f'input: ({i}, {j}, {l}) fails?')


if __name__ == '__main__':
    unittest.main()
