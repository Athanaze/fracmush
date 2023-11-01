import unittest
from fracmush import compute_replacement

class TestComputeReplacement(unittest.TestCase):
    def test_compute_replacement_empty_input(self):
        result = compute_replacement('')
        self.assertEqual(result, '')  # Expected output is an empty string.

    def test_compute_replacement_no_match(self):
        result = compute_replacement('This is a test string')
        self.assertEqual(result, 'This is a test string')  # No matches, input should be unchanged.

    def test_compute_replacement_single_match(self):
        result = compute_replacement('🍄Hello, World!🍄')
        self.assertEqual(result, 'Hello, World!888')  # Expected output with '888' appended.

    def test_compute_replacement_multiple_matches(self):
        input_str = '🍄Match1🍄 and 🍄Match2🍄'
        result = compute_replacement(input_str)
        self.assertEqual(result, 'Match1888 and Match2888')  # Both matches with '888' appended.

if __name__ == '__main__':
    unittest.main()
