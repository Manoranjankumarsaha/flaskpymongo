from application import api
from flask import jsonify
from flask_restx import Resource

ts = api.namespace('Testing', description='Testing...')
@ts.route('/')
class apiTesting(Resource):
    def get(self):
        return jsonify('Hello World!')