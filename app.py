from flask import Flask

app = Flask(__name__)

@app.route('/GET/<code>')
def main(code):
    return code

if __name__ == "__main__":
    app.run(debug=True)