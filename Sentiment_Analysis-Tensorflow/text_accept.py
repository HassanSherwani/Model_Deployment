from flask import Flask, render_template, flash, request, url_for, redirect, session
import numpy as np
import pandas as pd
import os
IMAGE_FOLDER = os.path.join('static')
app = Flask(__name__)

#model = load_model('sentiment_analysis_model.h5')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict/',methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        json_table = data.to_json(orient='records')
    return app.response_class(response=json_table,status=200,mimetype='application/json')

if __name__ == "__main__":
    #init()
    app.run(host='127.0.0.0',port=4000)
