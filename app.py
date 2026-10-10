from flask import Flask, make_response, request, render_template
from shortener import shorten
import storage

app = Flask(__name__)

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
    return "URL Added.", 201 

if __name__ == "__main__":
    storage.init_db()
    app.run(debug=True)