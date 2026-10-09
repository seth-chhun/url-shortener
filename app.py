from flask import Flask, make_response
from shortener import shorten
import storage

app = Flask(__name__)

@app.route('/GET/<code>')
def main(code):
    url, = storage.find_url(code)
    response = make_response()
    response.status_code = 302
    response.location = url
    return response

if __name__ == "__main__":
    storage.init_db()
    app.run(debug=True)