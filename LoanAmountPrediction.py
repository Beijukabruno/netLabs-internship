import pandas as pd
from flask import Flask, render_template, request,redirect
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder 
from sklearn.ensemble import RandomForestRegressor


# creating our flask instance
app = Flask(__name__)

# Load the dataset
# df = pd.read_csv('loans.csv')

df = pd.read_csv('/home/beijuka/INTERNSHIP/financial-inclusion-in-africa/loans.csv')


#an alternative approaches
# df['location_country_code'].fillna('Unknown', inplace=True)

# most_frequent_country_code = df['location_country_code'].mode().iloc[0]
# df['location_country_code'].fillna(most_frequent_country_code, inplace=True)

# Drop rows with missing location_country_code
# df = df.dropna(subset=['location_country_code'])

#Fill ing in missing values using the forward fill approach
df['location_country_code'].fillna(method='ffill', inplace=True)
# Select relevant features and target variable
X = df[['lender_count', 'repayment_term', 'sector','status','location_country_code']] 
y = df['loan_amount'] 

# Encode categorical features using One-Hot Encoding
encoder = OneHotEncoder(drop='first')
X_encoded = encoder.fit_transform(X)

# Create a Linear Regression model
# model = LinearRegression()

# Create a RandomForestRegression model
model = RandomForestRegressor()
model.fit(X_encoded, y)


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

    # Encode the user input using the same OneHotEncoder to resolve the errors 
    user_input = encoder.transform([[lender_count, repayment_term, sector, status, location_country_code]]).toarray()

    # Make prediction using the model
    prediction = model.predict(user_input)[0]

    # rounding up to predicted amount
    rounded_amount = round(prediction, 3)

    # our predicted amount in dollars rounded to 3dps
    dollar_prediction = "$ {:.3f}".format(rounded_amount)

    return render_template('index.html', prediction=dollar_prediction)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
# incase the port is already in use

    # app.run(debug=True, port=8080)
    # app.run(debug=True, port=8000)
    # app.run(debug=True, port=5000)

