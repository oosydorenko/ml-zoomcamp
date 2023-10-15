import pickle
import json

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model2.bin'
dv_file = 'dv.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

with open(dv_file, 'rb') as f_in:
    dv = pickle.load(f_in)

app = Flask('credit')

def predict(client):
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    
    return y_pred


def predict_q3():
    client = json.loads('{"job": "retired", "duration": 445, "poutcome": "success"}')
    print(f'client:{client}')

    credit = predict(client)
    print(f'score:{credit}')


@app.route('/predict', methods=['POST'])
def predict_q4():
    client = request.get_json()
    print(f'client:{client}')

    credit = predict(client)
    print(f'score:{credit}')
    result = {
        'credit_probability': float(credit)
    }

    return jsonify(result)


#predict_q3()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)