from flask import Flask, render_template, flash, request, url_for, redirect, session
import numpy as np
import pandas as pd
import re
import os
import tensorflow as tf
from numpy import array
from keras.datasets import imdb
#from tensorflow.keras.models import sequence
#from tensorflow.keras.models import load_model

from keras.preprocessing import sequence
from keras.models import load_model

#IMAGE_FOLDER = os.path.join('static')
app = Flask(__name__)



def init():
    global model,graph
    # load the pre-trained Keras model
    model = load_model('sentiment_analysis_model.h5')
    graph = tf.compat.v1.get_default_graph()

#########################Code for Sentiment Analysis ###############
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        text = request.form['text']
        data = [text]
        result=data
        result=pd.DataFrame(result,columns=["text"])
        x_test=result["text"]
        MAX_NB_WORDS = 2000
        # Max number of words in each complaint.
        MAX_SEQUENCE_LENGTH = 140
        # This is fixed.
        EMBEDDING_DIM = 50
        tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
        tokenizer.fit_on_texts(x_test.values)
        X_token = tokenizer.texts_to_sequences(x_test.values)
        X_test_pad = pad_sequences(X_token,maxlen=MAX_SEQUENCE_LENGTH)
        prediction = model.predict(X_test_pad)[:, 1]
        pred_class = model.predict_classes(X_test_pad, verbose=0)

        # using dataframe
        output = data
        output= pd.DataFrame(output, columns=["text"])
        output["sentiment-type"] = pred_class
        output["sentiment-type"] = output['sentiment-type'].map({1: "positive", 0: "negative"})
        output["probability"] = prediction
        json_table = result.to_json(orient='records')
    return app.response_class(
        response=json_table,
        status=200,
        mimetype='application/json'
    )

    #return app.response_class(response=json_table,status=200,mimetype='application/json')
    #return render_template('result.html',probability=probability)
    #return render_template('home.html', text=result["text"], probability=prediction)

#########################Code for Sentiment Analysis

if __name__ == "__main__":
    init()
    app.run(host='0.0.0.0',port=4000)
