from flask import request, jsonify
from functools import wraps
import jwt

import runtime
import todo

import controllers.users

app = None

def todo_service_init (flask_app):
	global app
	app = flask_app

def token_required (f):
	@wraps (f)
	def decorator (*args, **kwargs):
		token = request.headers.get ("Authorization")
		if not token:
			return jsonify ({"error": "Missing token"}), 401
		try:
			print (token)
			token = token[len ("Bearer "):]
			print (token)
			data = jwt.decode (token, app.config.get ("PUB_KEY"), algorithms='RS256')
			decoded_user = controllers.users.todo_user_load_from_decoded_data (data)
		except Exception as e:
			if todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT:
				print (e)

			return jsonify ({"error": "Invalid token"}), 401

		return f (decoded_user, *args, **kwargs)
	return decorator
