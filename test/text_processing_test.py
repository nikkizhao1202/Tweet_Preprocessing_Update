"""
pytest text_processing.py

"""
import unittest
from pre_processing.text_processing import TextProcessor

class Test(unittest.TestCase):
    """
    pytest text_processing

    """
    def setUp(self):
        """
        Call Text Processor Library
        """
        self.textprocessor = TextProcessor()

    def test_clean_text(self):
        """
        Test wheter clean text properly

        """
        text = 'I love you from the Moon and back #hahaha @li'
        expected_result = 'I love you from the Moon and back  '
        result = self.textprocessor.clean_text(text)
        self.assertEqual(result, expected_result)

    def test_tokenize_text(self):
        """
        Test wether text being tokenized properly
        """
        text = 'i love from the moon and back'
        expected_result = ['love','moon','back']
        result = self.textprocessor.tokenize_text(text)
        self.assertEqual(result, expected_result)



