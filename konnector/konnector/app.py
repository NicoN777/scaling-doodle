import os

from flask import Flask, make_response, request, jsonify
from konnector.handler import owner, application, login as user_login, session as user_session
from konnector.model import Owner, User, Response, Application

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'knktr')
KONNECTOR_SK = app.secret_key


KONNECTOR_SESSION_NAME = f'{app.secret_key}-session'


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/login', methods=["POST"])
def login():
    if not user_login.is_session_alive(request.cookies.get(KONNECTOR_SESSION_NAME)):
        return _bodyless_response_builder(user_login.start(request.form))
    print('Session is good')
    response = make_response()
    response.status_code = 200
    return response

@app.route('/owner/register', methods=["POST"])
def owner_register():
    return _response_builder(owner.register(User.from_keys(**request.get_json())))


@app.route('/owner', methods=["GET"])
def get_owner_by_id():
    return _response_builder(owner.get_owners())


@app.route('/application/register', methods=["POST"])
def application_register():
    return _response_builder(application.register(Application.from_keys(**request.get_json())))


def _bodyless_response_builder(intermediate_response: Response):
    response = make_response()
    response.status_code = intermediate_response.http_code
    response.set_cookie(key=KONNECTOR_SESSION_NAME, value=intermediate_response.data[KONNECTOR_SESSION_NAME])
    return response
def _response_builder(intermediate_response: Response):
    response = make_response(intermediate_response.serialize())
    response.status_code = intermediate_response.http_code
    return response


if __name__ == '__main__':
    app.run(port=7000, debug=True)
