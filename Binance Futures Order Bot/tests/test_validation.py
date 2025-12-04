import unittest
import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils import validate_quantity, validate_price

class TestValidation(unittest.TestCase):
    def test_validate_quantity_positive(self):
        valid, val = validate_quantity(10)
        self.assertTrue(valid)
        self.assertEqual(val, 10.0)

    def test_validate_quantity_string(self):
        valid, val = validate_quantity("0.5")
        self.assertTrue(valid)
        self.assertEqual(val, 0.5)

    def test_validate_quantity_negative(self):
        valid, msg = validate_quantity(-1)
        self.assertFalse(valid)
        self.assertIn("must be positive", msg)

    def test_validate_quantity_invalid(self):
        valid, msg = validate_quantity("abc")
        self.assertFalse(valid)
        self.assertIn("valid number", msg)

    def test_validate_price_positive(self):
        valid, val = validate_price(50000)
        self.assertTrue(valid)
        self.assertEqual(val, 50000.0)

    def test_validate_price_negative(self):
        valid, msg = validate_price(-100)
        self.assertFalse(valid)
        self.assertIn("must be positive", msg)

if __name__ == '__main__':
    unittest.main()
