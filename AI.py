from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample training data
texts  = ["I love this movie", "Terrible film", "Great performance", "Bad acting"]
labels = [1, 0, 1, 0]  # 1=positive, 0=negative

# Build a pipeline: TF–IDF → Naive Bayes
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('nb',    MultinomialNB())
])

# Train
model.fit(texts, labels)

# Predict
print(model.predict(["What a fantastic film!"]))  # e.g. [1]
