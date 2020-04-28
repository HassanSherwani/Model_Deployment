import numpy as np
from flask import Flask, abort , jsonify , request
from sklearn import datasets
import pickle

iris = datasets.load_iris()
model_rfc=pickle.load(open("iris_model.pkl","rb"))

app=Flask(__name__)

# Route
@app.route('/')
def index():
	return"Basic API for Iris classification"

# api route
#@app.route('/api/', methods=["GET"])
#def get_data():
#	return jsonify({"iris_data": iris})

# api route if we want to take query i.e value of type of classes

@app.route('/api/', methods=['POST'])

def make_predict():
    #all kind of error checking
    data=request.get_json(force=True)
    #convert json to numpy array
    predict_request=[data['sl'],data['sw'],data['pl'],data['pw']]
    predict_request=np.array(predict_request)
    # np array goes to random forest model, prediction is outcome
    y_hat=model_rfc.predict(predict_request)
    # reurn prediction output
    output=[y_hat[0]]
    return jsonify(results=output)

if __name__ == '__main__':
	app.run(debug=True)