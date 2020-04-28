from flask import Flask,jsonify,make_response,abort
import json
from flask_restful import Api, Resource

# init app
app = Flask(__name__)

# create small datasets
books = [{"id": 1,"title":"whatever1",},{"id":2,"tietle":"whatever2",}]

# Using External Local Data
with open("books.json") as f:
	books_json = json.load(f)

# Route
@app.route('/')
def index():
	return"Basic API for query of book information using titles and their index"

# api route
@app.route('/api/v1/books', methods=["GET"])
def get_book():
	return jsonify({"books": books})

# api route if we want to take query i.e index from user

@app.route('/api/v1/books/<int:id>', methods=["GET"])
def get_book_index(id):
	book=[book for book in books if book['id'] == id]
	return jsonify({"books":book})

# version 2 is for loaded json file

@app.route('/api/v2/books', methods=["GET"])
def get_book_json():
	return jsonify({"books": books_json})

# api route using title as query

@app.route('/api/v2/books/<string:title>' , methods=['GET'])
def get_book_title(title):
	book_json_img = [book for book in books_json if book["title"] == title]
	return jsonify({"books":book_json_img})

if __name__ == '__main__':
	app.run(debug=True)