from flask import Flask, make_response, request, redirect, render_template, flash, url_for, abort
from app.shortener import shorten
import app.storage as storage
import os
from dotenv import load_dotenv
from app.url import check_url
import urllib3

def create_app():

    storage.init_db()

    load_dotenv()

    app = Flask(__name__)
    app.secret_key = os.environ.get('FLASK_SECRET_KEY')

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == "POST":
            try:
                url = check_url(request.form['url'], request.root_url)
            except urllib3.exceptions.LocationParseError:
                flash("URL too long.", 'error')
                return redirect(request.referrer)
            except RecursionError:
                flash("Self-Referencing is not allow.", 'error')
                return redirect(request.referrer)
            except TimeoutError:
                flash("Invalid URL.", 'error')
                return redirect(request.referrer)
            
            url = str(url)

            while True:
                code = shorten(url)
                try:
                    storage.insert(code, url)
                    break
                except ReferenceError as e:
                    violation = str(e)
                    print(violation)

                    if violation == "collision.url":
                        code, = storage.find_code(url)
                        break
                    elif violation == "collision.code":
                        continue
                        
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

    return app

