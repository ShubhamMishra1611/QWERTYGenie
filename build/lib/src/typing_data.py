from typing import List, Tuple
from analysis import TypingAnalyzer

class TypingSession:
    def __init__(self):
        self.analyzer = TypingAnalyzer()
        self.keystrokes = []

    def simulate_typing(self, sentences: List[Tuple[str, str]]):
        """
        Simulate user typing for testing purposes.

        :param sentences: A list of tuples where each tuple contains the sentence typed and the correct sentence.
        """
        for typed_sentence, expected_sentence in sentences:
            self._process_sentence(typed_sentence, expected_sentence)

    def _process_sentence(self, typed_sentence: str, expected_sentence: str):
        """
        Process a sentence to extract unigrams, bigrams, and trigrams.
        
        :param typed_sentence: The sentence typed by the user.
        :param expected_sentence: The correct sentence.
        """
        n = len(expected_sentence)
        
        for i in range(n):
            typed_unigram = typed_sentence[i:i+1]
            expected_unigram = expected_sentence[i:i+1]
            self.analyzer.record_keystroke(typed_unigram, expected_unigram)

        for i in range(n-1):
            typed_bigram = typed_sentence[i:i+2]
            expected_bigram = expected_sentence[i:i+2]
            self.analyzer.record_keystroke(typed_bigram, expected_bigram)

        for i in range(n-2):
            typed_trigram = typed_sentence[i:i+3]
            expected_trigram = expected_sentence[i:i+3]
            self.analyzer.record_keystroke(typed_trigram, expected_trigram)

    def get_problematic_sequences(self, threshold: float):
        """
        Identify problematic sequences after the typing session.
        
        :param threshold: The weighted error score threshold.
        :return: A dictionary of problematic sequences and their scores.
        """
        return self.analyzer.identify_problematic_sequences(threshold)
