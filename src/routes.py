from .functions import *
from flask import request, Response, Blueprint
import json

models_api = Blueprint('face_detection_api', __name__)

@models_api.route('/predict', methods=['POST'])
def prediction():
    body = request.get_json(silent=True)
    project = 'plataformas-cognitivas-386718'

    if len(body['instance']) == 0 or 'instance' not in body.keys():
        print(body.keys())
        print(body['instance'])
        raise Exception('Nenhuma instância recebida')

    if 'model' not in body.keys():
        raise Exception('Modelo não está no body')

    if 'version' not in body.keys():
        raise Exception('Versão não está no body')

    results = predict_json(
        project=project,
        model=body['model'],
        version=body['version'],
        instances=body['instance']
    )

    if body['model'] == 'model_deepL':
        results = [value['dense_2'][0] for value in results]

    return Response(json.dumps({"result": results}), status=200, mimetype="application/json")