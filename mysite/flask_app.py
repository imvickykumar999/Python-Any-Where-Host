
from flask import Flask, render_template, jsonify
from firebase_admin import db
import firebase_admin


app = Flask(__name__)
app.jinja_env.globals.update(zip=zip)


def run():
    file = 'ideationology.json'
    cred = firebase_admin.credentials.Certificate(file)

    url = 'https://ideationology-4c639-default-rtdb.asia-southeast1.firebasedatabase.app/'
    path = {'databaseURL' : url}

    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred, path)

    refv = db.reference('pythonanywhere/views')
    g = refv.get() +1

    refv.set(g)
    return g, url


@app.route('/')
def index():
    views = run()[0]
    return jsonify({"Page view": str(views)}), 200


if __name__ == '__main__':
    app.secret_key = "123"
    app.run(debug=True)


# bash : 
# https://www.pythonanywhere.com/user/imvickykumar999/consoles/28083905/
