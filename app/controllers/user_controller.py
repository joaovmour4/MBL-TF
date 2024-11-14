from flask import Blueprint, request, jsonify
from app.models.user_model import User

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/create', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User.create_user(
        name=data['name'],
        email=data['email']
    )
    return jsonify(user), 201

@user_controller.route('/all', methods=['GET'])
def get_users():
    users = User.get_users()
    if users:
        return jsonify(users)
    else:
        return jsonify({'error': 'User not found'}), 404
    
@user_controller.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.get_user_by_id(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404