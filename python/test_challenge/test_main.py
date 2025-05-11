import unittest
import solution


class TestMain(unittest.TestCase):
    def test_basic_addition(self):
        result = solution.add_numbers(2, 3)
        self.assertEqual(result, 5)
        result = solution.add_numbers(-1, 1)
        self.assertEqual(result, 0)
        result = solution.add_numbers(0, 0)
        self.assertEqual(result, 0)

    def test_large_numbers(self):
        self.assertEqual(solution.add_numbers(999999, 1), 1000000)
        self.assertEqual(solution.add_numbers(-500000, 500000), 0)

    def test_negative_numbers(self):
        self.assertEqual(solution.add_numbers(-5, -7), -12)
        self.assertEqual(solution.add_numbers(-3, 10), 7)

    def test_return_type(self):
        self.assertIsInstance(solution.add_numbers(1, 2), int)

    def test_invalid_input_types(self):
        with self.assertRaises(TypeError):
            solution.add_numbers("1", 2)
        with self.assertRaises(TypeError):
            solution.add_numbers(1.5, 2)


if __name__ == "__main__":
    unittest.main()
