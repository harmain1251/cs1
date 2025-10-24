from flask import Flask, jsonify, render_template
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# List of jokes
jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "I told my computer I needed a break, and it said ‘No problem — I’ll go to sleep.’",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why do cows wear bells? Because their horns don’t work!",
    "Why did the math book look sad? Because it had too many problems.",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
    "Parallel lines have so much in common… it’s a shame they’ll never meet."
]

@app.route('/')
def home():
    # Serve the HTML joke page
    return render_template('index.html')

@app.route('/joke')
def get_joke():
    return jsonify({"joke": random.choice(jokes)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

