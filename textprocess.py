import nltk

# 1. Download resources (run these once)
nltk.download('punkt_tab')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def preprocess(text):
    tokens = word_tokenize(text)
    tokens = [t.lower() for t in tokens if t.isalpha()]
    sw = set(stopwords.words('english'))
    filtered = [t for t in tokens if t not in sw]
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



# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from nltk.stem import PorterStemmer

# nltk.download('punkt_tab')
# nltk.download('stopwords')

# def process_text(text):
#     tokens = word_tokenize(text.lower())
#     stopwords_list = set(stopwords.words('english'))
#     tokens = [word for word in tokens if word.isalnum() and word not in stopwords_list]
#     stemmer = PorterStemmer()
#     stemmed_tokens = [stemmer.stem(word) for word in tokens]
#     return stemmed_tokens

# # Example usage:
# text = "NLTK is a leading platform for building Python programs to work with human language data."
# processed_tokens = process_text(text)
# print("\nProcessed Tokens:")
# print(processed_tokens)
