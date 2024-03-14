import json
import pickle
import os

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
# Load the scaler object from the pickle file
scaler_path = os.path.join('model', 'scaler.pkl')
with open(scaler_path, 'rb') as f:
    scalar = pickle.load(f)
# Load the XGBoost model from its pickle file
xgb_model_path = os.path.join('model', 'best_xgb_os.pkl')
with open(xgb_model_path, 'rb') as f:
    xgb_model = pickle.load(f)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    
    time = float(data['Time'])
    amount = float(data['Amount'])
    
    # Scale 'Time' and 'Amount' features
    scaled_time = scalar.transform([[time]])[0][0]
    scaled_amount = scalar.transform([[amount]])[0][0]
    
    # Update the 'Time' and 'Amount' values with the scaled values
    data['Time'], data['Amount'] = scaled_time, scaled_amount
    # Make predictions using the trained model
    new_data = np.array(list(data.values())).reshape(1, -1)
    output = xgb_model.predict(new_data)
    print(output[0])
    return jsonify(str(output[0]))


    
if __name__ == '__main__':
    app.run(debug=True)
    