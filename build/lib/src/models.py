import random
from llama_index.llms.gemini import Gemini
from prompts import PROMPT_GENERATE_SENTENCE

from dotenv import load_dotenv

load_dotenv()

llm = Gemini(model="models/gemini-pro")

def generate_sentence_with_ngram(ngram: str) -> str:
    """
    Use LLM to generate a sentence containing the given n-gram.
    
    :param ngram: The n-gram to include in the sentence.
    :return: A sentence containing the n-gram.
    """
    prompt = PROMPT_GENERATE_SENTENCE.format(ngram=ngram)
    response = llm.complete(prompt)
    print(f'Here is the {response = }')
    sentence = response.text.strip()
    
    # if not sentence or ngram not in sentence:
    #     sentence = generate_random_sentence_with_ngram(ngram)
    return sentence

def generate_practice_sentences(problematic_sequences):
    """
    Generate practice sentences containing the problematic sequences using the LLM.
    
    :param problematic_sequences: Dictionary of problematic sequences and their error metrics.
    :return: A list of practice sentences.
    """
    practice_sentences = []
    for ngram_type, ngram in problematic_sequences.keys():
        sentence = generate_sentence_with_ngram(ngram)
        practice_sentences.append(sentence)
    
    return practice_sentences

def generate_random_sentence_with_ngram(ngram: str) -> str:
    """
    Generate a random fallback sentence that contains the given n-gram.
    
    :param ngram: The n-gram to include in the sentence.
    :return: A random fallback sentence containing the n-gram.
    """
    sentence_templates = [
        f"The {ngram} was found in the wild.",
        f"It is common to see {ngram} in the text."
    ]
    return random.choice(sentence_templates)
