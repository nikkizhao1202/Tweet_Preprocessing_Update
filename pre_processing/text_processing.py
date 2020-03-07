'''
Import all the modules needed for text preprocessing

'''
import re
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords

class TextProcessor():
    """
    Pre Processor class
    """
    def __init__(self):
        """
        setup the pre processor with URL regex and Twitter Pre Processor

        """

        p_1 = r'https?:\/\/[\S\/]*'
        p_2 = r'#[\S]*'
        p_3 = r'@[\S]*'
        p_4 = r'\s?rt'
        p_5 = r'\n+'
        p_6 = r'\s?[0-9]\s?'
        self.text_regex = f'({p_1})|({p_2})|({p_3})|({p_4})|({p_5})|({p_6})'
        self.tokenizer = TweetTokenizer(strip_handles=True, reduce_len=True, preserve_case=False)
        self.stopwords = stopwords.words('english')

    def clean_text(self, input_text):
        """
        Clean input text

        """
        text = re.sub(self.text_regex, '', input_text, flags=re.MULTILINE)
        text = re.sub(r'won\'t', 'will not', text)
        text = re.sub(r'can\'t', 'can not', text)
        text = re.sub(r'didn\'t', 'did not', text)
        text = re.sub(r'\'s', ' is', text)
        text = re.sub(r'\'m', ' am', text)
        text = re.sub(r'\'re', ' are', text)
        text = re.sub(r'\'ve', ' have', text)
        text = re.sub(r'\'ll', ' will', text)
        text = re.sub(r'\'d', ' would', text)
        text = re.sub(r'\'t', ' not', text)
        cleaned_text = re.sub(r'n\'t', ' not', text)

        return cleaned_text

    def tokenize_text(self, input_text):
        """
        Tokenize the input_Text with class tokenizer

        """
        tokens = self.tokenizer.tokenize(input_text)
        tokens = [word for word in tokens if word not in self.stopwords]

        return tokens
