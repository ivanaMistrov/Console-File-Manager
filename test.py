import unittest
import math

class TestFilter(unittest.TestCase):
    def test_filter_even_numbers(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
        self.assertEqual(filtered_numbers, [2, 4, 6, 8, 10])

    def test_filter_positive_numbers(self):
        numbers = [-1, -2, 0, 1, 2]
        filtered_numbers = list(filter(lambda x: x > 0, numbers))
        self.assertEqual(filtered_numbers, [1, 2])


class TestMap(unittest.TestCase):
    def test_map_square(self):
        numbers = [1, 2, 3, 4, 5]
        squared_numbers = list(map(lambda x: x^2, numbers))
        self.assertEqual(squared_numbers, [1, 4, 9, 16, 25])

    def test_map_convert_to_string(self):
        numbers = [1, 2, 3, 4, 5]
        strings = list(map(str, numbers))
        self.assertEqual(strings, ['1', '2', '3', '4', '5'])


class TestSorted(unittest.TestCase):
    def test_sorted_ascending_order(self):
        numbers = [4, 2, 1, 3, 5]
        sorted_numbers = sorted(numbers)
        self.assertEqual(sorted_numbers, [1, 2, 3, 4, 5])

    def test_sorted_descending_order(self):
        numbers = [4, 2, 1, 3, 5]
        sorted_numbers = sorted(numbers, reverse=True)
        self.assertEqual(sorted_numbers, [5, 4, 3, 2, 1])


class TestMath(unittest.TestCase):
    def test_pi(self):
        self.assertAlmostEqual(math.pi, 3.14159, places=5)

    def test_sqrt(self):
        self.assertEqual(math.sqrt(4), 2)

    def test_pow(self):
        self.assertEqual(math.pow(2, 3), 8)

    def test_hypot(self):
        self.assertEqual(math.hypot(3, 4), 5)

if __name__ == '__main__':
    unittest.main()
