from flask import Flask, request, render_template, jsonify
from textblob import TextBlob
import ssl
import requests
import random

requests.packages.urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Randomly determine the sentiment
    sentiment_text = random.choice(["Positive", "Negative", "Neutral"])

    result = {
        "sentiment": sentiment_text,
        "text": text
    }
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
