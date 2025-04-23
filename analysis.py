import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag, FreqDist
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger_eng')

def extract_features_nltk_sklearn(text):
    # Tokenization
    words = word_tokenize(text)
    sentences = sent_tokenize(text)

    # Filter out punctuation tokens
    words_alpha = [word for word in words if word.isalpha()]

    # Stopwords
    stop_words = set(stopwords.words("english"))
    stopword_count = sum(1 for word in words_alpha if word.lower() in stop_words)

    # POS tagging
    pos_tags = pos_tag(words_alpha)
    pos_fd = FreqDist(tag for (word, tag) in pos_tags)

    # Lexical stats
    word_count = len(words_alpha)
    unique_words = len(set(words_alpha))
    char_count = sum(len(word) for word in words_alpha)
    avg_word_length = char_count / word_count if word_count else 0
    hapax_legomena = len([w for w in FreqDist(words_alpha).hapaxes()])

    # Sentence stats
    sentence_count = len(sentences)
    avg_sentence_length = word_count / sentence_count if sentence_count else 0

    return {
        "word_count": word_count,
        "unique_word_count": unique_words,
        "char_count": char_count,
        "avg_word_length": avg_word_length,
        "stopword_count": stopword_count,
        "hapax_legomena": hapax_legomena,
        "sentence_count": sentence_count,
        "avg_sentence_length": avg_sentence_length,
        "pos_distribution": dict(pos_fd)
    }

# Example text
text = "Apple is looking at buying a startup. It may cost them a billion dollars."

features = extract_features_nltk_sklearn(text)
for key, value in features.items():
    print(f"{key}: {value}")