import google.auth
import googleapiclient.discovery


def predict_json(project, model, instances, version=None):
    credentials, project_id = google.auth.load_credentials_from_file('src/static/token.json')

    service = googleapiclient.discovery.build('ml', 'v1', credentials=credentials)
    name = 'projects/{}/models/{}'.format(project, model)

    if version is not None:
        name += '/versions/{}'.format(version)

    response = service.projects().predict(
        name=name,
        body={'instances': instances}
    ).execute()

    if 'error' in response:
        raise RuntimeError(response['error'])

    return response['predictions']
