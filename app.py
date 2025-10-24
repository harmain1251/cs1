from flask import Flask, jsonify, render_template
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # allows HTML pages from other origins to access this API

# List of quotes
quotes = [
    "The best way to get started is to quit talking and begin doing. – Walt Disney",
    "Don’t let yesterday take up too much of today. – Will Rogers",
    "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
    "If you are working on something exciting, it will keep you motivated. – Steve Jobs",
    "Success is not in what you have, but who you are. – Bo Bennett",
    "Act as if what you do makes a difference. It does. – William James",
    "With the new day comes new strength and new thoughts. – Eleanor Roosevelt"
]

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/quote')
def quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

