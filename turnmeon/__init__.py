from flask import Flask
from flask_restful import Api

from turnmeon.v1.control import Control


def create_app():

    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Control,"/v1/control/", endpoint="api.turmeon.v1.control")

    return app
