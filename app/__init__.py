from os import getenv
from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from config import config_env

app = Flask(__name__)

app.config.from_object(config_env[getenv('FLASK_ENV')])


authorizations = {
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    app,
    title='Boilerplate Flask',
    version='0.0.1',
    description='Endpoints de nuestro boilerplate',
     authorizations=authorizations,
    doc='/swagger-ui'
)

CORS(app)
