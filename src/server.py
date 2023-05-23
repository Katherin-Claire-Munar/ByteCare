from flask import Flask, request, jsonify
from flask_cors import CORS
from main import randomforest

app = Flask(__name__)
CORS(app)

@app.route('/randomforest')
def run_randomforest():
    # Call the randomforest function and get the result
    symptoms = request.args

  # Extract the symptoms from the query parameters
    symptom1 = symptoms.get("symptom1")
    #symptom2 = symptoms.get("symptom2")
    #symptom3 = symptoms.get("symptom3")
    #symptom4 = symptoms.get("symptom4")
    #symptom5 = symptoms.get("symptom5")

    # Prepare the result as a JSON object
    result_json = {
        #'result': randomforest(symptom1, symptom2, symptom3, symptom4, symptom5),
        'result': randomforest(symptom1),
    }

    # Set the Content-Type header to application/json
    response = jsonify(result_json)
    response.headers['Content-Type'] = 'application/json'

    return response

if __name__ == '__main__':
    app.run()
