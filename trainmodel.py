import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

# Sample dataset (Replace with real anonymization data)
data = {
    "text": ["My name is John", "I live in Paris", "Anonymous user reported this", "Hidden identity"],
    "label": [0, 0, 1, 1],  # 1 = Anonymized, 0 = Not Anonymized
}

df = pd.DataFrame(data)

# Split data
X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.2, random_state=42)

# Build pipeline (TF-IDF + Naive Bayes)
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", MultinomialNB()),
])

# Train model
model.fit(X_train, y_train)

# Save model
with open("deanonymizationprevention/backend/model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")
