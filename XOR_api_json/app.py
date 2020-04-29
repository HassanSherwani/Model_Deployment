import numpy as np
import pickle
from flask import Flask , request , jsonify

def predict_xor_output(num1,num2):

    output={'output_prediction_of_xor' : 0}
    x_input = np.array([num1,num2]).reshape(1,2)
    filename='xor_model.pkl'
    m1=pickle.load(open(filename, 'rb'))
    output['output_prediction_of_xor']=m1.predict(x_input)[0]
    print(output)
    return output

app=Flask(__name__)

@app.route('/')
def index():
    return "XOR Prediction API"

@app.route("/xor_prediction", methods=['GET'])
def cal_xor_predict():
    body=request.get_data()
    header=request.headers

    try:
        num1=int(request.args['x1'])
        num2=int(request.args['x2'])
        if (num1 != None) and (num2 != None) and ((num1 == 0)) and ((num2==0)) or ((num2==1)):
            res=predict_xor_output(num1,num2)
        else:
            res= {
                'success' : False,
                'message': 'Input data is not correct'}
    except:
        res={
            'success': False,
            'message':'unknown error'}
    return jsonify(res)

if __name__ == '__main__':
	app.run(debug=True)