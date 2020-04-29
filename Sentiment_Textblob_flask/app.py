from flask import Flask, render_template,request,url_for
from flask_bootstrap import Bootstrap

# NLP Packages
from textblob import TextBlob,Word
import random
import time

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')
# for analyse
@app.route('/analyse')
def analyse():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)


