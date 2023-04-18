from application import api
from flask import jsonify
from flask_restx import Resource,fields

# Create a new namespace for the API
usr_ns = api.namespace('user', description='User API')

# Define the data model for your API
user_model = usr_ns.model('User', {
    'name': fields.String(required=True, description='enter your name'),
    'email': fields.String(required=True, description='enter your email id'),
    'password': fields.String(required=True, description='enter your password')
})
dummy_obj={'key':"value"}

# Define a class for handling API requests
@usr_ns.route('/')
class UserGetAndPost(Resource):
    # @usr_ns.marshal_list_with(user_model)
    def get(self):
        '''List all items'''
        return jsonify('Hello World!')
    @api.expect(user_model)
    @usr_ns.marshal_with(user_model)
    def post(self):
        '''Create a new item'''
        payload = api.payload
        # return {'message': 'User Account already register'}, 401
        # return book, 201
        return jsonify(payload)

@usr_ns.route('/<int:idx>')
@usr_ns.response(404, 'user not found')
class UserGetOnePutDelete(Resource):
    def get(self, idx):
        '''Shows a single user item and lets you delete it'''
        if idx==1:
            #return {'message': 'User not found'}, 404
            return jsonify(dummy_obj)
        usr_ns.abort(404, "User {} doesn't exist".format(idx))
    
    def put(self, idx):
        '''Delete an example given its id'''
        if idx==1:
            # return {'message': 'Incorrect password'}, 401
            return jsonify(dummy_obj)
        usr_ns.abort(404, "User {} doesn't exist".format(idx))
             
    def delete(self, idx):
        '''Delete an example given its id'''
        if idx==1:
            # return '', 204
            return jsonify(dummy_obj)
        usr_ns.abort(404, "User {} doesn't exist".format(idx))