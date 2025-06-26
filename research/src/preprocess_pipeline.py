from preprocess import *
from config import preprocessing_config

def preprocess_text(text, config):
    # Step 0: Handle emojis (before tokenization)
    if config['handle_emojis']:
        text = handle_emojis(text)

    # Step 1: Tokenize
    tokens = tokenize(text)

    # Step 2: Apply each preprocessing step conditionally
    if config['lowercase']:
        tokens = lowercase(tokens)

    if config['remove_punctuation']:
        tokens = remove_punctuation(tokens)

    if config['remove_stopwords']:
        tokens = remove_stopwords(tokens)

    if config['handle_negations']:
        tokens = handle_negations(tokens)

    if config['stemming']:
        tokens = stem_tokens(tokens)

    if config['lemmatization']:
        tokens = lemmatize_tokens(tokens)

    return ' '.join(tokens)  # Return cleaned text as a string

result = preprocess_text("I do NOT like this product!  It's not good at all!!! Lionel Messi" , preprocessing_config )

print(result)