import unittest
from giftdecider import Child


class GiftTests(unittest.TestCase):
    def test_bad(self):
        """Tests the child creation and gift calculation for a bad child."""
        test_child = Child("V", 12, 5, 90)

        self.assertEqual(test_child.name, "V")
        self.assertFalse(test_child.is_under_ten)
        self.assertEqual(test_child.good, 5)
        self.assertEqual(test_child.bad, 90)

        test_child.calc_gift()

        self.assertIsNotNone(test_child.ratio)
        self.assertLess(test_child.ratio, 0)
        self.assertFalse(test_child.gets_gift)
        self.assertIsNone(test_child.wrapping_paper_color)

        self.assertIn("V", test_child.status())
        self.assertNotIn("wrapping paper", test_child.status())

    def test_good_younger(self):
        """Tests the child creation and gift calculation for a good child under 10."""
        pass

    def test_good_older(self):
        """Tests the child creation and gift calculation for a good child over 10."""
        pass

    def test_good_equals_bad(self):
        """Tests the gift calculation when a child was equally good and bad."""
        pass

    def test_invalid_args(self):
        """Tests the Child constructor with invalid arguments."""
        pass

if __name__ == "__main__":
    unittest.main()
