from collections import defaultdict
from typing import Dict, Tuple

class TypingAnalyzer:
    def __init__(self, alpha: float = 1.0, beta: float = 1.5):
        """
        Initialize the TypingAnalyzer with specified weights for the weighted error score.
        
        :param alpha: Weight for error frequency in the weighted error score.
        :param beta: Weight for error rate in the weighted error score.
        """
        self.alpha = alpha
        self.beta = beta
        self.unigram_data = defaultdict(lambda: {'errors': 0, 'total': 0})
        self.bigram_data = defaultdict(lambda: {'errors': 0, 'total': 0})
        self.trigram_data = defaultdict(lambda: {'errors': 0, 'total': 0})

    def record_keystroke(self, typed: str, expected: str):
        """
        Record a keystroke, comparing the typed character or sequence with the expected one.

        :param typed: The sequence typed by the user.
        :param expected: The expected correct sequence.
        """
        if len(expected) == 1:
            self._update_data(self.unigram_data, typed, expected)
        elif len(expected) == 2:
            self._update_data(self.bigram_data, typed, expected)
        elif len(expected) == 3:
            self._update_data(self.trigram_data, typed, expected)
        

    def _update_data(self, data: Dict[str, Dict[str, int]], typed: str, expected: str):
        """
        Update the error frequency and total counts for a given sequence.
        
        :param data: The data dictionary to update (unigram, bigram, or trigram).
        :param typed: The sequence typed by the user.
        :param expected: The expected correct sequence.
        """
        data[expected]['total'] += 1
        if typed != expected:
            data[expected]['errors'] += 1
        
    def calculate_error_metrics(self) -> Dict[str, Tuple[float, float, float]]:
        """
        Calculate the error frequency, error rate, and weighted error score for all sequences.

        :return: A dictionary containing error metrics for each sequence.
        """
        results = {}
        
        for sequence_type, data in [('unigram', self.unigram_data),
                                    ('bigram', self.bigram_data),
                                    ('trigram', self.trigram_data)]:
            for sequence, metrics in data.items():
                E_f = metrics['errors']
                N = metrics['total']
                E_r = E_f / N if N > 0 else 0
                W_e = self.alpha * E_f + self.beta * E_r
                results[(sequence_type, sequence)] = (E_f, E_r, W_e)
        
        return results

    def identify_problematic_sequences(self, threshold: float) -> Dict[str, float]:
        """
        Identify sequences with a weighted error score above a given threshold.
        
        :param threshold: The threshold for identifying problematic sequences.
        :return: A dictionary of problematic sequences with their weighted error scores.
        """
        problematic_sequences = {}
        metrics = self.calculate_error_metrics()
        
        for (sequence_type, sequence), (E_f, E_r, W_e) in metrics.items():
            if W_e > threshold:
                problematic_sequences[(sequence_type, sequence)] = W_e
                
        return problematic_sequences

