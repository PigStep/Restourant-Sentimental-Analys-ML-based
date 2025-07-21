import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import joblib
import numpy as np

nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
class TextPreprocessor:
    @staticmethod
    def clean_text(text):
        text = text.lower()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        return text

    @staticmethod
    def tokenizeTxt(text):
        return word_tokenize(text)

    @staticmethod
    def remove_stopwords(tokens):
        stop_words = set(stopwords.words('english'))
        negations = {"no", "not", "never", "none", "nobody", "neither", "nor"}
        stop_words = stop_words - negations
        return [word for word in tokens if word.casefold() not in stop_words]

    @staticmethod
    def lemmatize(tokens):
        lemmatizer = WordNetLemmatizer()
        return [lemmatizer.lemmatize(word, pos='v') for word in tokens]

    @staticmethod
    def merge_negative_tokens(tokens):
        skip = False
        negations = {"no", "not", "never", "none", "nobody", "neither", "nor"}
        merge = []
        for i in range(len(tokens)):
            if skip:
                skip = False
                continue
            if tokens[i] in negations and i+1 < len(tokens):
                skip = True
                merge.append(f"{tokens[i]}_{tokens[i+1]}")
                continue
            merge.append(tokens[i])
        return merge

    def preprocess(self, text):
        text = self.clean_text(text)
        tokens = self.tokenizeTxt(text)
        tokens = self.remove_stopwords(tokens)
        tokens = self.lemmatize(tokens)
        tokens = self.merge_negative_tokens(tokens)
        return ' '.join(tokens)

global preprocessText

def preprocessText(text):
    preprocessor = TextPreprocessor()
    return preprocessor.preprocess(text)

class TextClassifier:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)
        self.preprocessor = TextPreprocessor()
    
    def predict(self, text):
        processed_text = self.preprocessor.preprocess(text)
        return {
            "prediction": int(self.model.predict([processed_text])),
            "confidence": np.max(self.model.predict_proba([processed_text]))
        }