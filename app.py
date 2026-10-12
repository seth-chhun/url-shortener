from flask import Flask, make_response, request, redirect, render_template, flash, url_for, abort
from shortener import shorten
import storage
import os
from dotenv import load_dotenv
from url import check_url

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        url = check_url(request.form['url'])
        
        if url is None:
            flash("Invalid URL.", 'error')
            return redirect(request.referrer)
        
        url = str(url)
        code = shorten(url)

        storage_insertion = storage.insert(code, url)
        
        if storage_insertion == False:
            code, = storage.find_code(url)

        flash("".join([request.url_root, code]), 'success')
        
        return redirect(request.referrer)

    return render_template('index.html')
    

@app.route('/<code>')
def redirect_to_url(code):
    try:
        url, = storage.find_url(code)
        response = make_response()
        response.status_code = 302
        response.location = url
        return response
    except TypeError:
        abort(404)

if __name__ == "__main__": 
    storage.init_db()
    app.run(debug=True)