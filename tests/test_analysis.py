import unittest
from src.analysis import TypingAnalyzer
from src.typing_data import TypingSession

class TestTypingAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = TypingAnalyzer()

    def test_unigram_error_detection(self):
        # Simulate recording a typing error for unigrams
        self.analyzer.record_keystroke('t', 't')
        self.analyzer.record_keystroke('e', 'h')
        self.analyzer.record_keystroke('s', 's')
        
        metrics = self.analyzer.calculate_error_metrics()
        
        # Check if the error was recorded correctly
        self.assertEqual(metrics[('unigram', 't')], (0, 0.0, 0.0))
        self.assertEqual(metrics[('unigram', 'h')], (1, 1.0, 2.5))  # 1 error, error rate 1.0

    def test_bigram_error_detection(self):
        # Simulate recording a typing error for bigrams
        self.analyzer.record_keystroke('te', 'te')
        self.analyzer.record_keystroke('eh', 'he')
        
        metrics = self.analyzer.calculate_error_metrics()
        
        # Check if the error was recorded correctly
        self.assertEqual(metrics[('bigram', 'te')], (0, 0.0, 0.0))
        self.assertEqual(metrics[('bigram', 'he')], (1, 1.0, 2.5))  # 1 error, error rate 1.0

    def test_trigram_error_detection(self):
        # Simulate recording a typing error for trigrams
        self.analyzer.record_keystroke('the', 'the')
        self.analyzer.record_keystroke('eh ', ' he')
        
        metrics = self.analyzer.calculate_error_metrics()
        
        # Check if the error was recorded correctly
        self.assertEqual(metrics[('trigram', 'the')], (0, 0.0, 0.0))
        self.assertEqual(metrics[('trigram', ' he')], (1, 1.0, 2.5))  # 1 error, error rate 1.0

    def test_identify_problematic_sequences(self):
        # Simulate recording some keystrokes
        self.analyzer.record_keystroke('a', 'a')
        self.analyzer.record_keystroke('b', 'c')
        self.analyzer.record_keystroke('c', 'c')
        
        problematic_sequences = self.analyzer.identify_problematic_sequences(threshold=2.0)
        
        # Check if the problematic sequence is identified
        self.assertIn(('unigram', 'c'), problematic_sequences)

class TestTypingSession(unittest.TestCase):

    def setUp(self):
        self.session = TypingSession()

    def test_unigram_bigram_trigram_processing(self):
        # Simulate a typing session with errors
        self.session.simulate_typing([
            ("teh", "the"),  # errors in both unigrams and bigrams
            ("brwn", "brown"),  # error in trigram
        ])
        
        problematic_sequences = self.session.get_problematic_sequences(threshold=0)
        
        # Check if problematic sequences are correctly identified
        self.assertIn(('unigram', 't'), problematic_sequences)
        self.assertIn(('bigram', 'te'), problematic_sequences)
        self.assertIn(('trigram', 'bro'), problematic_sequences)

    def test_no_errors_detected(self):
        # Simulate a typing session without errors
        self.session.simulate_typing([
            ("the", "the"),
            ("brown", "brown"),
        ])
        
        problematic_sequences = self.session.get_problematic_sequences(threshold=0)
        
        # There should be no problematic sequences
        self.assertEqual(len(problematic_sequences), 0)

if __name__ == '__main__':
    unittest.main()
