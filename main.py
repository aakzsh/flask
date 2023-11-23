from flask import Flask, jsonify
import os
import pandas as pd
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/check')
def checkk():
    return "99"    

@app.route("/test")
def test():
    return jsonify({"sender_score": 0.421, "receiver_score": 0.1112, "overall_score": 0.232})


@app.route('/calculate/<fromm>/<to>/<amount>')
def check(fromm, to, amount):
    
    input1 = pd.DataFrame({
        'account_no': [int(fromm)],
        'credit_amount': [0],
        'debit_amount': [int(amount)],
        'transaction_type': 0
    })

    input2 = pd.DataFrame({
        'account_no': [int(to)],
        'credit_amount': [int(amount)],
        'debit_amount': [0],
        'transaction_type': 1
    })

    model = pickle.load(open('model3.pkl', 'rb'))
    prob1 = model.predict_proba(input1)
    prob2 = model.predict_proba(input2)

    return jsonify({"sender_score": prob1[0][0], "receiver_score": prob2[0][0], "overall_score": prob1[0][0]*0.5+prob2[0][0]*0.5})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))


# dummy input
# new_input = pd.DataFrame({
#     'account_no': [409000611074],
#     'credit_amount': [0],
#     'debit_amount': [125000],
#     'transaction_type': 1
# })    
