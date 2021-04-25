from flask import Blueprint, jsonify, request

from errors import *
import runtime
import todo

import controllers.users

users = Blueprint ('users', __name__)

# GET /api/users
@users.route ('/api/users', methods=['GET'])
def users_handler ():
	return jsonify ({'msg': "Users works!"}), 200

# POST /api/users/register
@users.route ('/api/users/register', methods=['POST'])
def users_register_handler ():
	result = controllers.users.todo_users_register (request)

	if result == TODO_ERROR_NONE:
		return jsonify ({'msg': "Created a new user!"}), 200

	else:
		return todo_error_send_response (result)

# POST /api/users/login
@users.route ('/api/users/login', methods=['POST'])
def users_login_handler ():
	error, user = controllers.users.todo_users_login (request)

	if error == TODO_ERROR_NONE:
		return controllers.users.todo_user_generate_token (user)

	else:
		return todo_error_send_response (result)
