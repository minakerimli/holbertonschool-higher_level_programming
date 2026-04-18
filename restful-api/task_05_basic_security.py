from flask_jwt_extended import JWTManager
from flask import jsonify

jwt = JWTManager(app)


@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401
