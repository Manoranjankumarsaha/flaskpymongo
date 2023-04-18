import logging

from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
from flask_restx import Api
from flask_cors import CORS
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer
from flask_jwt_extended import JWTManager

app=Flask(__name__)
app.config.from_object(Config)

db=MongoEngine()
db.init_app(app)

mail = Mail(app)

serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
# cors = CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:3000"}})

api=Api()
api.init_app(app)

jwt = JWTManager(app)

api.namespaces = []

from application import logger
from application import route_test ,route_user,route_example,route_item,route_jwt
from application.route import emp