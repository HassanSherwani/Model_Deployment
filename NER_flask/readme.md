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


# API

/api/Text [GET]
Text should be submitted as phrase key (/api/phrase?phrase=).
[{"raw text": "Facebook is our supplier and bol.com is client in this example".}]

/api/deliverable [POST]
Expects a raw text, .docx, .txt,.pdf file object, returns html with sentences and highlighted entities:

[{"Text":"Facebook is our supplier and bol.com is client in this example", {"entity":"Facebook"},"label":"Supplier"}]


/api/deliverable-lines [POST]
Expects text submitted as form key, returns html with sentences and extracted entities 


