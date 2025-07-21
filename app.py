from flask import Flask, render_template, request
import re
from textblob import TextBlob  # Упрощённый анализ тональности

app = Flask(__name__)

def analyze_sentiment(text):
    """Упрощённый анализ тональности (можно заменить на вашу модель)"""
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity  # -1 (негатив) до 1 (позитив)
    
    if polarity > 0.1:
        return "positive", round(polarity, 2)
    elif polarity < -0.1:
        return "negative", round(abs(polarity), 2)
    else:
        return "neutral", 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        sentiment, confidence = analyze_sentiment(text)
        return render_template('index.html', 
                             text=text,
                             sentiment=sentiment,
                             confidence=confidence)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)