"""
pytest word_embedding.py

"""
import unittest
import os
from pre_processing.word_embedding import WordEmbedding


class Test(unittest.TestCase):
    """
    pytest word embedding
    """

    def setUp(self):
        """
        call wordembedding lib
        """
        self.embeddings = WordEmbedding(max_dictionary_size = 1000)
        self.embedding_dictionary = self.embeddings.load_embedding_dictionary(self.embeddings.dictionary_path)

    def test_load_embedding_dictionary_resource(self):
        """

        Testing proper embedding loading from resource dictionary 

        """

        self.embeddings.load_embedding_dictionary(self.embeddings.dictionary_path)
        self.assertEqual(len(self.embeddings.embedding_dictionary),1000)

    def test_load_from_zip(self):
        """
        test whether can load zip file

        """

        zip_resource = os.path.join(
            self.embeddings.dictionary_path.replace("glove.twitter.txt", "test_resources.zip"),
            "pre_processing","..",
            "test_resources", "glove.twitter.txt")

        self.embeddings.load_embedding_dictionary(zip_resource)
        self.assertEqual(len(self.embeddings.embedding_dictionary),1000)


    def test_replace_tokens_with_index(self):
        """
        Testing proper token replacement

        """

        token_list = ['love', '<user>', 'moon', 'back']
        expected_result = [56, 2, 1, 98]
        result = self.embeddings.replace_tokens_with_index(token_list)
        self.assertEqual(result, expected_result)

