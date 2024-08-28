import streamlit as st
from typing_data import TypingSession
from models import generate_practice_sentences
import time

# Initialize TypingSession and state variables
session = TypingSession()
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'reference_sentence' not in st.session_state:
    st.session_state.reference_sentence = "The quick brown fox jumps over the lazy dog."
if 'previous_text' not in st.session_state:
    st.session_state.previous_text = ""

# Streamlit UI
st.title("Typing Master with LLM Integration")

# Input box for typing practice
if st.session_state.start_time is None:
    st.session_state.start_time = time.time()

typed_text = st.text_area("Type the following sentence:", "", key="typed_text")

# Calculate typing speed
if len(st.session_state.previous_text) > 0:
    elapsed_time = time.time() - st.session_state.start_time
    words_typed = len(st.session_state.previous_text.split())
    typing_speed = (words_typed / elapsed_time) * 60  # Words per minute (WPM)
else:
    typing_speed = 0.0

# Button to submit the typed text
if st.button("Analyze Typing"):
    # Reset the typing session and start time
    session = TypingSession()
    st.session_state.start_time = time.time()

    # Simulate real typing session with actual user input
    session.simulate_typing([(typed_text, st.session_state.reference_sentence)])

    # Analyze and identify problematic sequences
    threshold = 2.0
    problematic_sequences = session.get_problematic_sequences(threshold)

    # Generate a new reference sentence with problematic n-grams using LLM
    if problematic_sequences:
        practice_sentences = generate_practice_sentences(problematic_sequences)
        print(f'{practice_sentences = }')
        if practice_sentences:
            st.session_state.reference_sentence = practice_sentences[0]  # Use the first generated sentence
            st.write("New practice sentence generated! Try typing this:")
        else:
            st.write("Failed to generate practice sentences with LLM.")
    else:
        st.write("No significant errors detected! You can retry or finish.")
    
    st.session_state.previous_text = typed_text
    st.session_state.start_time = None  # Reset start time for the next round

# Display the new or initial reference sentence
st.subheader("Reference Sentence:")
st.write(st.session_state.reference_sentence)

# Display typing speed
st.subheader("Typing Speed:")
st.write(f"Your typing speed: {typing_speed:.2f} WPM")
