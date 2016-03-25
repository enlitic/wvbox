import wvbox
import unittest
import os

INPUT_WV_FILE = os.path.join(os.path.dirname(__file__),
                             "word_vectors_test.txt")
INPUT_STRING = "hi these are some words surprise"

class SimpleTokenizer(object):
    def analyze(self, input_string):
        return input_string.split()


class WVBoxTestCase(unittest.TestCase):
    def setUp(self):
        self.wv = wvbox.WVBox(tokenizer=SimpleTokenizer())
        self.wv.load_vectors(INPUT_WV_FILE)

    def tearDown(self):
        self.wv = None

    def test_loading_header_error(self):
        with self.assertRaises(ValueError):
            self.wv.build(header=False)

    def test_loading_with_header(self):
        self.wv.build(header=True)
        idx = self.wv.get_indices(INPUT_STRING)
        words = self.wv.get_words(idx)
        self.assertListEqual(
            words,
            ["hi", "these", "are", "some", "words", "<unk>"]
        )
        
        
