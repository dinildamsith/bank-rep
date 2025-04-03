from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd


# Load the model file
model = joblib.load('bank_model.joblib')

# Initialize the Flask app
app = Flask(__name__)

@app.route("/")
def clientDetailsFillForm():
    return render_template('clientDetailsFillForm.html')

@app.route("/predict", methods=['POST'])
def getPrediction():
    try:
        # Extract form data
        age = request.form['age']
        job = request.form['job']
        marital = request.form['marital']
        education = request.form['education']
        credit_default = request.form['default']
        housing = request.form['housing']
        loan = request.form['loan']
        duration = request.form['duration']  # Fixed mistake

        # Convert to dictionary
        data = {
            'age': age,
            'job': job,
            'marital': marital,
            'education': education,
            'default': credit_default,
            'housing': housing,
            'loan': loan,
            'duration': duration,
        }

        # 🚀 Replace this with actual prediction logic
        predictions = model.predict(pd.DataFrame([data]))

        return jsonify({'prediction': predictions.tolist()})  # Return JSON response

    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Return error message if something goes wrong

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)