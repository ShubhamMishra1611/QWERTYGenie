import unittest
from src.models import generate_sentence_with_ngram

class TestLLMIntegration(unittest.TestCase):
    def test_generate_sentence_with_ngram(self):
        # Test cases with some example n-grams
        test_ngrams = ['quick', 'brown fox', 'lazy dog']
        for ngram in test_ngrams:
            sentence = generate_sentence_with_ngram(ngram)
            print(f"Generated sentence for '{ngram}': {sentence}")
            self.assertIn(ngram, sentence, f"'{ngram}' not found in generated sentence.")

if __name__ == "__main__":
    unittest.main()
