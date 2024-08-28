from typing_data import TypingSession
from models import generate_practice_sentences

def main():
    # Simulate a typing session
    session = TypingSession()
    
    # Simulate user typing data (typed, expected)
    sentences = [
        ("teh quikc brown fx", "the quick brown fox"),
        ("lbme dg", "lazy dog"),
        ("teh quikc brown fx", "the quick brown fox")
    ]
    
    session.simulate_typing(sentences)
    
    threshold = 1.0
    problematic_sequences = session.get_problematic_sequences(threshold)
    
    practice_sentences = generate_practice_sentences(problematic_sequences)
    
    print("Practice Sentences:")
    for sentence in practice_sentences:
        print(sentence)

if __name__ == "__main__":
    main()
