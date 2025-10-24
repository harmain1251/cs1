from flask import Flask, jsonify, render_template
import random
import datetime
import json
import os

app = Flask(__name__, template_folder="templates")

QUOTES_FILE = os.path.join(os.path.dirname(__file__), "quotes.json")
with open(QUOTES_FILE, "r", encoding="utf-8") as f:
    QUOTES = json.load(f)

def get_daily_quote():
    today = datetime.date.today().toordinal()
    idx = today % len(QUOTES)
    return QUOTES[idx]

@app.route("/")
def index():
    quote = get_daily_quote()
    return render_template("index.html", quote=quote)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/api/quote/today")
def api_quote():
    quote = get_daily_quote()
    return jsonify({
        "date": str(datetime.date.today()),
        "quote": quote
    })

if __name__ == "__main__":
    # Added a print statement for Jenkins test
    print("Jenkins trigger test")
    app.run(host="0.0.0.0", port=8080)
    
