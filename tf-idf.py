from sklearn.feature_extraction.text import TfidfVectorizer

# Sample corpus: list of raw text documents
corpus = [
    "The cat sat on the mat",
    "The dog ate my homework",
    "Cats and dogs are great"
]

# Initialize the vectorizer
vectorizer = TfidfVectorizer(
    lowercase=True,      # convert all text to lowercase
    stop_words='english' # optionally remove English stopwords
)

# Learn vocabulary and idf, then return TF–IDF matrix
tfidf_matrix = vectorizer.fit_transform(corpus)

# feature names (terms)
terms = vectorizer.get_feature_names_out()

# Convert to a dense array and print as rows = docs, columns = terms
print("Terms:", list(terms))
print("\nTF–IDF matrix:\n", tfidf_matrix.toarray())
