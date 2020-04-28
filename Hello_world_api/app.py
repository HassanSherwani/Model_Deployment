from flask import Flask,jsonify,make_response,abort
import json
from flask_restful import Api, Resource

# init app
app = Flask(__name__)

# Route
@app.route('/')
def index():
	return"hello world"

if __name__ == '__main__':
	app.run(debug=True)