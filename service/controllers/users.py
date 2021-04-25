from flask import request

from errors import *
import runtime
import todo

from models.user import *

def todo_user_get_by_email (email):
	found = user_get_by_email (email)
	if (found is not None):
		return user_parse (found)

	return None

def todo_users_register (request):
	error = TODO_ERROR_NONE

	if (request.json is not None):
		email = request.json['email']
		name = request.json['name']
		username = request.json['username']
		password = request.json['password']
		confirm = request.json['confirm']

		if (email and name and username and password and confirm):
			found = user_get_by_email (email)
			if (found is None):
				# if todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT:
				# 	print ("name: ", name)
				# 	print ("username: ", username)
				# 	print ("email: ", email)
				# 	print ("password: ", password)
				# 	print ("confirm: ", confirm)

				if (password == confirm):
					user = user_create (email, name, username, password)
					saved_user = user_insert (user)

					print ("Created a new user!")
					print (user)

				else:
					print ("Passwords do not match!")
					error = TODO_ERROR_BAD_REQUEST
				
			else:
				print ("User already exists!")
				error = TODO_ERROR_EXISTING_USER

		else:
			error = TODO_ERROR_MISSING_VALUES

	else:
		error = TODO_ERROR_MISSING_VALUES

	return error
