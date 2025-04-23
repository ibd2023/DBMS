import nltk

# 1. Download resources (run these once)
nltk.download('punkt_tab')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def preprocess(text):
    # --- Tokenization ---
    tokens = word_tokenize(text)
    
    # keep only alphabetic tokens & lowercase them
    tokens = [t.lower() for t in tokens if t.isalpha()]
    
    # --- Stopword Removal ---
    sw = set(stopwords.words('english'))
    filtered = [t for t in tokens if t not in sw]
    
    # --- Stemming ---
    stemmer = PorterStemmer()
    stemmed = [stemmer.stem(t) for t in filtered]
    
    return tokens, filtered, stemmed

if __name__ == '__main__':
    sample = (
        "This is an example sentence, showing off the stop words "
        "filtration and stemming process!"
    )
    orig, no_sw, stems = preprocess(sample)

    print("Original Tokens:       ", orig)
    print("After Stopword Removal:", no_sw)
    print("After Stemming:        ", stems)
