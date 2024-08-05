import unittest
from fracmush import compute_replacement

class TestComputeReplacement(unittest.TestCase):
    # def test_compute_replacement_empty_input(self):
    #     result = compute_replacement('')
    #     self.assertEqual(result, '')  # Expected output is an empty string.

    # def test_compute_replacement_single_match(self):
    #     result = compute_replacement('simple.replacement')
    #     self.assertEqual(result, 'just some long text meant to be put in as is')

    # def test_compute_replacement_single_match(self):
    #     result = compute_replacement('simple.replacement $')
    #     self.assertEqual(result, 'just some long text meant to be put in as is')

    def test_compute_replacement_single_match2(self):
        result = compute_replacement('simple.replacement $ MORE TEXT HERE')
        self.assertEqual(result, 'just some long text meant to be put in as is MORE TEXT HERE')
if __name__ == '__main__':
    unittest.main()
