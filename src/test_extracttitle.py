import unittest
from extracttitle import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_find_h1(self):
        self.assertEqual(extract_title(test1), result1)
        self.assertEqual(extract_title(test1_1), result1)
        self.assertEqual(extract_title(test2), result2)
    def test_raises_no_h1(self):
        with self.assertRaises(Exception):
            extract_title(test3)
            extract_title(test4)




test1 = "# This is a basic test"
test1_1 = "#    This is a basic test   "
result1 = "This is a basic test"
test2 = """## This one tests differentiation
# because the header is on another line"""
result2 = "because the header is on another line"
test3 = "This tests what happens if there is no header"
test4 = "   # This should raise an exceptiopn too"

if __name__ == "__main__":
    unittest.main()