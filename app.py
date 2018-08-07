from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
@app.route('/')
def index():
    url = "http://thecatapi.com/api/images/get?format=src&type=gif"
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="127.0.0.1")
