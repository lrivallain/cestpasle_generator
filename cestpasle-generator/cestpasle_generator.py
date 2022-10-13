"""Main module."""

import random
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def quote():
    with open('data/quotes.txt', 'r') as f:
        quotes = f.readlines()
    return render_template('index.html', quote=escape(random.choice(quotes)))
