"""Main module."""

import random
from flask import Flask, render_template, make_response, send_from_directory
from markupsafe import escape

app = Flask(__name__)


def get_quote():
    """Return a random quote from data

    Returns:
        str: a random quote
    """
    with open("data/quotes.txt", "r", encoding="utf-8") as file:
        quotes = file.readlines()
    return random.choice(quotes).strip()

@app.route('/')
@app.route('/html')
def quote():
    with open('data/quotes.txt', 'r') as f:
        quotes = f.readlines()
    return render_template('index.html', quote=escape(get_quote()))

@app.route('/plain')
@app.route('/raw')
@app.route('/txt')
def metrics():
    response = make_response(get_quote(), 200)
    response.mimetype = "text/plain"
    return response

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
   app.run()
