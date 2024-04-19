import re
import unicodedata
from collections import Counter
import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from joblib import load
import os


class DataPreprocessor:
    def __init__(self):
        self.stopwords = set(stopwords.words('spanish'))
        self.stemmer = SnowballStemmer('spanish')

    def clean_text(self, text):
        # Eliminar etiquetas HTML
        text = re.sub('<[^>]*>', '', text)
        # Eliminar tildes y otros caracteres especiales
        text = ''.join((c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn'))
        # Convertir a minúsculas
        text = text.lower()
        # Encontrar emoticones
        emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
        # Eliminar caracteres no alfanuméricos
        text = re.sub('[\W]+', ' ', text) + ' '.join(emoticons).replace('-', '')
        return text.split()

    def remove_stopwords(self, words):
        return [w for w in words if w not in self.stopwords]

    def delete_rare_words(self, words):
        vocabulary = Counter(words)
        rare_words = set(word for word, count in vocabulary.items() if count == 1)
        return [w for w in words if w not in rare_words]

    def stem_words(self, words):
        return [self.stemmer.stem(word) for word in words]

    def preprocess(self, text):
        text = self.clean_text(text)
        text = self.remove_stopwords(text)
        text = self.stem_words(text)
        text = self.delete_rare_words(text)
        return ' '.join(text)


class ReviewClassifier:
    def __init__(self):
        self.pipeline = load('BestModel.pkl')
        self.preprocessor = DataPreprocessor()
        self.vectorizer = load('Vectorizer.pkl')


    def predict(self, review):
        processed_review = self.preprocessor.preprocess(review)
        vectorized_review = self.vectorizer.transform([processed_review])
        lets_see = self.pipeline.predict(vectorized_review)
        return self.pipeline.predict(vectorized_review)

classifier = ReviewClassifier()

def classify_review(text):
    prediction = classifier.predict(text)
    # The prediction is an array of strings, we change each element to an integer
    return int(prediction[0])

def classify_reviews(texts_df: pd.DataFrame) -> pd.DataFrame:
    num_columns = texts_df.shape[1]
    if num_columns == 1:
        texts_df.columns = ['Review']
        texts_df['Score'] = texts_df['Review'].apply(classify_review)
    else:
        raise Exception('Invalid number of columns in the DataFrame. Only one column is allowed.')

    return texts_df