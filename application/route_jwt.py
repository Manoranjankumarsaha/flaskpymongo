from application import app
from flask import jsonify,request
from flask_restx import Resource,fields
from flask_jwt_extended import create_access_token, jwt_required,get_jwt_identity

@app.route('/login', methods=['POST'])
def login():
    app.logger.info('This is an info message.')
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username != 'admin' or password != 'password':
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    # return {'access_token': access_token}, 200
    return jsonify(access_token=access_token)

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({'hello': 'world'})

@app.route('/check_jwt')
@jwt_required
def check_jwt():
    #Authorization: Bearer <access_token>
    current_user = get_jwt_identity()
    return jsonify({'message': f'Hello, {current_user}!'})

