from flask import Flask, jsonify
from flask_cors import CORS

def create_app(settings_override=None):
    """[Create a Flask application using the app factory patter]

    :return: Flask app
    """

    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)
    if settings_override:
        app.config.update(settings_override)

    @app.route('/')
    def index():
        """[]
        """
        return jsonify({'name': 'Hello World!'})

    return app
