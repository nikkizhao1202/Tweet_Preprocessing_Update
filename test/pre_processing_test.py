"""
pytest pre_processing.py

"""
import unittest
from pre_processing.pre_processing import PreProcessor


class Test(unittest.TestCase):
    """
    pytest preprocessing
    """
    def setUp(self):
        self.pre_processor = PreProcessor(padding_size=20)

    def test_pad_sequence(self):
        """
        Testing whether sequence in same padding length
        """
        sequence = [1,2,3,4,5]
        expected_sequence = [1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        output = self.pre_processor.pad_sequence(sequence)

        self.assertEqual(output, expected_sequence)

    def test_divide(self):
        """
        test
        """
        result = self.pre_processor.pre_process_text('I <user> am hewei Yang! :),, !!!')
        expected_result = [2, 1, 149, 11, 1, 6, 6, 11, 11, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result, expected_result)
