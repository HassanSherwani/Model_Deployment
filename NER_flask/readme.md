# Problem Statement

- Extracting key entities using flask

# Installation

Recommended start is miniconda (python 3.6).
Install dependencies with:
```bash
conda install flask numpy gensim scipy spacy scikit-learn gunicorn
conda install docx2txt -c conda-forge
```
**gensim** is optional and needed only if you use topic modeling or word2vec models.
- Don't forget to python -m spacy download en to install the spaCy language pack.

# Deployment

Recommended deployment stack is gunicorn (+ nginx) where gunicorn serves as uwsgi server.
Note that models are loaded only when first request is initiated. If your guincorn timeout is too aggressive the models
will never load and the system will just go into a loop. Check gunicorn_settings.py.example for safe settings or if you want to use the
same settings just simply run:
```bash
cp gunicorn_settings.py.example gunicorn_settings.py # adjust the contents if needed
gunicorn -c phrase-API/gunicorn_settings.py phrase-API.wsgi
```

# API

/api/phrase [GET]
Phrases should be submitted as phrase key (/api/phrase?phrase=). It returns 50 most similar phrases (trained on
contractual documents). Lower means more similar phrase.
[{"distance": "0.1", "phrase": "similar phrase 1"},{...}]

/api/deliverable [POST]
Expects a docx file object, returns JSON with sentences and probabilities that a sentence is a D&O:
[{"sentence":"This is a sentence", "proba":0.3}, {"sentence":"This is a second sentence", "proba":0.35}]
Higher proba (probability) means higher likelihood that a sentence is a D&O.

/api/deliverable-lines [POST]
Expects text submitted as form key, returns JSON with sentences and probabilities that a sentence is a D&O:
[{"sentence":"This is a sentence", "proba":0.3}, {"sentence":"This is a second sentence", "proba":0.35}]


