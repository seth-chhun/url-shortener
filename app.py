from flask import Flask, make_response, request, render_template, flash
from shortener import shorten
import storage
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<code>')
def redirect(code):
    url, = storage.find_url(code)
    response = make_response()
    response.status_code = 302
    response.location = url
    return response

@app.route('/', methods=['POST'])
def submit():
    url = request.form['url']
    shorten(url)
    code, = storage.find_code(url)
    flash("".join([request.base_url, code]), 'success')
    return render_template('index.html'), 201 

if __name__ == "__main__":
    storage.init_db()
    app.run(debug=True)