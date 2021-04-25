from flask import jsonify

TODO_ERROR_NONE = 0
TODO_ERROR_BAD_REQUEST = 1
TODO_ERROR_MISSING_VALUES = 2
TODO_ERROR_BAD_USER = 3
TODO_ERROR_EXISTING_USER = 4
TODO_ERROR_SERVER_ERROR = 5

def todo_error_send_response (todo_error):
	response = None

	if (todo_error == TODO_ERROR_NONE):
		pass

	if (todo_error == TODO_ERROR_BAD_REQUEST):
		response = jsonify ({'error': "Bad request!"}), 400

	if (todo_error == TODO_ERROR_MISSING_VALUES):
		response = jsonify ({'error': "Missing values!"}), 400

	if (todo_error == TODO_ERROR_BAD_USER):
		response = jsonify ({'error': "Bad user!"}), 400

	if (todo_error == TODO_ERROR_EXISTING_USER):
		response = jsonify ({'error': "User already exists!"}), 400

	if (todo_error == TODO_ERROR_SERVER_ERROR):
		response = jsonify ({'error': "Server error!"}), 500

	return response
