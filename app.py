# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ["POST"])
def predict():
    """
    FOR RENDERING RESULTS ON HTMKL GUI
    """
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    predictions = model.predict(final_features)
    
    output = round(predictions[0], 2)
    return render_template('index.html', prediction_text = 'Employee Salary should be $ {}'.format(output))


@app.route('/predict_api', methods=['POST'])
def predict_api():
    """
    FOr direct api calls through requests

    """
    data = request.get_json(force=True)
    predictions = model.predict([np.array(list(data.values()))])
    
    outputs = predictions[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)