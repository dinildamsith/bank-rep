from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd


# Load the model file
model = joblib.load('../bank_model.joblib')

# Initialize the Flask app
app = Flask(__name__)

@app.route("/")
def clientDetailsFillForm():
    return render_template('clientDetailsFillForm.html')

@app.route("/predict", methods=['POST'])
def getPrediction():
    age =  request.form['age']
    job = request.form['job']
    marital = request.form['marital']
    education = request.form['education']
    default = request.form['default']
    housing = request.form['housing']
    loan = request.form['loan']
    duration = request.form['housing']
    
    data = {
         'age': age,
         'job':job,         # Encoded job category
         'marital': marital,      # Encoded marital status
         'education': education,    # Encoded education level
         'default': default,      # No credit in default
          'housing': housing,      # No housing loan
         'loan':loan,         # No personal loan
         'duration': duration,    # Last contact duration in seconds
    }
    
    
    
    predictions = model.predict(pd.DataFrame([data]))
    
    # # Convert predictions to a list
    # predictions_list = predictions.tolist()
    
    return render_template('clientDetailsFillForm.html', pred=predictions)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)