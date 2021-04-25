import json

from flask import request

from errors import *
import runtime
import todo

from models.item import *

def todo_items_get_all_by_user (user):
	return items_get_all_by_user (user.id)

def todo_item_get_by_id_and_user (item_id, user):
	found = item_get_by_id_and_user (item_id, user.id)
	if (found is not None):
		return item_parse (found)

	return None

def todo_item_get_by_id_and_user_to_json (user, item_id):
	return item_get_by_id_and_user_to_json (
		item_id, user.id
	)

def todo_item_create (user, request):
	error = TODO_ERROR_NONE

	if (request.json is not None):
		title = request.json['title']
		description = request.json['description']

		if (title and description):
			item = item_create (title, description, user.id)
			item_insert (item)
		else:
			error = TODO_ERROR_MISSING_VALUES

	else:
		error = TODO_ERROR_MISSING_VALUES

	return error

def todo_item_update (user, item_id, request):
	error = TODO_ERROR_NONE

	if (request.json is not None):
		title = request.json['title']
		description = request.json['description']

		if (title and description):
			item = todo_item_get_by_id_and_user (
				item_id, user
			)

			if (item):
				item.title = title
				item.description = description
				if (item_update (item) is False):
					error = TODO_ERROR_SERVER_ERROR

			else:
				error = TODO_ERROR_BAD_REQUEST
			
		else:
			error = TODO_ERROR_MISSING_VALUES

	else:
		error = TODO_ERROR_MISSING_VALUES

	return error

def todo_item_delete_by_id_and_user (user, item_id):
	return item_delete_by_id_and_user (
		item_id, user.id
	)
