import pandas as pd
import numpy as np
from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression
import joblib

app = Flask(__name__)

# Load the saved model from the file
# loaded_model = joblib.load('LoanAmountPredictionModel.pkl')
loaded_model = joblib.load('/home/beijuka/INTERNSHIP/Assignment/LoanAmountPredictionModel.pkl')
# encoder = loaded_model.named_steps['onehotencoder']
encoder = joblib.load('/home/beijuka/INTERNSHIP/Assignment/OneHotEncoder.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    lender_count = int(request.form['lender_count'])
    repayment_term = int(request.form['repayment_term'])
    sector = request.form['sector']
    status = request.form['status']
    location_country_code = request.form['location_country_code']

    # Encode the user input using the same OneHotEncoder
    user_input = encoder.transform([[lender_count, repayment_term, sector, status, location_country_code]]).toarray()

    # Make prediction using the loaded model
    prediction = loaded_model.predict(user_input)[0]

    # Round the prediction and format it as a dollar amount
    # rounded_prediction = "${:.2f}".format(round(prediction, 2))

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True,port=8080)
