from flask import Flask
from app.controllers.user_controller import user_controller

app = Flask(__name__)

app.register_blueprint(user_controller, url_prefix='/users')

from app.dynamodb import dynamodb