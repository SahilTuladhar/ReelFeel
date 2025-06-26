import re
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from emoji import demojize

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
nlp = spacy.load('en_core_web_sm')

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

# Tokenizer
def tokenize(text):
    return nltk.word_tokenize(text)

# Lowercase
def lowercase(tokens):
    return [token.lower() for token in tokens]

# Remove punctuation
def remove_punctuation(tokens):
    return [re.sub(r'[^\w\s]', '', token) for token in tokens if re.sub(r'[^\w\s]', '', token)]

# Stopword removal
def remove_stopwords(tokens):
    return [token for token in tokens if token.lower() not in stop_words]

# Stemming
def stem_tokens(tokens):
    return [stemmer.stem(token) for token in tokens]

# Lemmatization
def lemmatize_tokens(tokens):
    doc = nlp(' '.join(tokens))
    return [token.lemma_ for token in doc]

# Emoji handling
def handle_emojis(text):
    return demojize(text, delimiters=(" ", " "))

# Negation handling
def handle_negations(tokens):
    new_tokens = []
    skip_next = False
    for i in range(len(tokens)):
        if skip_next:
            skip_next = False
            continue
        if tokens[i].lower() == 'not' and i + 1 < len(tokens):
            new_tokens.append(f'not_{tokens[i+1]}')
            skip_next = True
        else:
            new_tokens.append(tokens[i])
    return new_tokens