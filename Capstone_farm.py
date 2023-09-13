# import pandas as pd
# from flask import Flask, render_template, request,redirect
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import OneHotEncoder 
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.preprocessing import MinMaxScaler

# # creating our flask instance
# app = Flask(__name__)

# df = pd.read_csv('/home/beijuka/INTERNSHIP/Assignment/Irrigation_dataset.csv')

# # separating features and target variable
# x = df[['CropDays', 'SoilMoisture', 'temperature','CropType']]
# y = df['Irrigation']

# # One-hot encode the 'CropType' feature
# encoded = pd.get_dummies(x, columns=['CropType'])
# encoded = encoded.astype(int)


# # Scale the entire encoded DataFrame (including CropType columns)
# scaler = MinMaxScaler(feature_range=(0, 1))
# x_scaled = scaler.fit_transform(encoded)


# # Split into test and train_data
# x_Train, x_test, y_Train, y_test = train_test_split(x_scaled, y, stratify=y, test_size=0.2, random_state=42)

# # Initialize the Random Forest Classifier
# rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# # Train the classifier on the training data
# rf_classifier.fit(x_Train,y_Train)

# if __name__ == '__main__':
#     app.run(debug=True, port=8080)


import pandas as pd
from flask import Flask, render_template, request, redirect
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# Creating our Flask instance
app = Flask(__name__)

# Load and preprocess the dataset
df = pd.read_csv('/home/beijuka/INTERNSHIP/Assignment/Irrigation_dataset.csv')
x = df[['CropDays', 'SoilMoisture', 'temperature', 'CropType']]
y = df['Irrigation']
encoded = pd.get_dummies(x, columns=['CropType'])
scaler = MinMaxScaler(feature_range=(0, 1))
x_scaled = scaler.fit_transform(encoded)
x_Train, x_test, y_Train, y_test = train_test_split(x_scaled, y, stratify=y, test_size=0.2, random_state=42)

# Initialize the Random Forest Classifier and train it
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(x_Train, y_Train)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    crop_days = float(request.form['crop_days'])
    soil_moisture = float(request.form['soil_moisture'])
    temperature = float(request.form['temperature'])
    crop_type = request.form['crop_type']

    # Perform one-hot encoding for crop_type
    encoded_crop_type = pd.get_dummies(pd.DataFrame({'CropType': [crop_type]}), columns=['CropType'])
    encoded_crop_type = encoded_crop_type.reindex(columns=encoded.columns, fill_value=0)

    # Combine all input features and scale them
    input_features = [[crop_days, soil_moisture, temperature]]
    input_features_scaled = scaler.transform(input_features)
    input_features_scaled = input_features_scaled.tolist()[0] + encoded_crop_type.values.tolist()[0]

    # Make the prediction
    prediction = rf_classifier.predict([input_features_scaled])[0]

    # Convert the prediction to a human-readable label
    result = "Irrigation needed" if prediction else "No irrigation needed"

    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
