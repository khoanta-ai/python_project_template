"""
Kiểm thử cho module calc.
"""

import unittest

from src.calc import add


class TestCalc(unittest.TestCase):
    """Kiểm thử các hàm trong module calc."""

    def test_add(self):
        """Kiểm thử hàm add với các giá trị mẫu."""
        result1 = add(2, 3)
        print(f"add(2, 3) = {result1}")
        self.assertEqual(result1, 5)
        result2 = add(-1, 1)
        print(f"add(-1, 1) = {result2}")
        self.assertEqual(result2, 0)


if __name__ == "__main__":
    unittest.main()
