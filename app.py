from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS
import joblib
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier


app = Flask(__name__)

CORS(app)

@app.route('/predict', methods=['POST'])
def predict():

    try:
        data = request.get_json(force=True)
        input_data = data['input_data']
        input_data = np.array(input_data).reshape((1, len(input_data)))
        col_names = ['Age', 'Height', 'Weight', 'family_history_with_overweight', 'FAVC', 'FCVC', 'NCP', 'CAEC', 'SMOKE', 'CH2O', 'FAF', 'TUE','CALC']
        df = pd.DataFrame(np.array(input_data), columns=col_names)
        scaler = joblib.load("minmax_scaler.pkl")
        input_data = scaler.transform(df)
        model = joblib.load("Gradient_boost")
        # Call your machine learning model to make predictions
        prediction = model.predict(input_data)
        # Return the prediction as JSON
        response_data = {"prediction": int(prediction[0])}
        return jsonify(response_data)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
