from flask import Flask, make_response, request, redirect, render_template, flash, url_for
from shortener import shorten
import storage
import os
from dotenv import load_dotenv
from url import check_url

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<code>')
def redirect_to_url(code):
    url, = storage.find_url(code)
    response = make_response()
    response.status_code = 302
    response.location = url
    return response

@app.route('/', methods=['POST'])
def submit():
    url = request.form['url']
    if check_url(url) is not None:
        url = str(check_url(url))
    code = shorten(url)
    storage.insert(code, url)
    flash("".join([request.base_url, code]), 'success')
    return redirect(request.referrer)

if __name__ == "__main__":
    storage.init_db()
    app.run(debug=True)