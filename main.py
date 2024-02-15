import math
from flask import Flask, request
from google.cloud import aiplatform

app = Flask(__name__)


def prediction(data):
    endpoint_id = 6887228686202830848
    project_id = 'sublime-state-413617'
    endpoint = aiplatform.Endpoint(f'projects/{project_id}/locations/us-central1/endpoints/{endpoint_id}')
    predict = endpoint.predict([data['instance']])
    return predict


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    predict = prediction(data)
    return {"prediction": math.floor(predict.predictions[0])}


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
