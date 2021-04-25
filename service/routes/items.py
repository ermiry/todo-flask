from flask import Blueprint, jsonify, request

from errors import *
import runtime
import todo

import controllers.items
import controllers.service
import controllers.users

items = Blueprint ('items', __name__)

# GET /api/todo/items
# get all the authenticated user's items
@items.route ('/api/todo/items', methods=['GET'])
@controllers.service.token_required
def todo_items_handler (decoded_user):
	result = controllers.items.todo_items_get_all_by_user (decoded_user)
	if (result is not None):
		return result, 200

	else:
		return jsonify ({
			"items": []
		}), 200

# POST /api/todo/items/register
# a user has requested to create a new item
@items.route ('/api/todo/items', methods=['POST'])
def todo_item_create_handler ():
	pass

# GET /api/todo/items/:id/info
# returns information about an existing item that belongs to a user
@items.route ('/api/todo/items/:id/info', methods=['GET'])
def items_login_handler ():
	pass

# PUT /api/todo/items/:id/update
# a user wants to update an existing item
@items.route ('/api/todo/items/:id/update', methods=['PUT'])
def todo_item_update_handler ():
	pass

# DELETE /api/todo/items/:id/remove
# deletes an existing user's item
@items.route ('/api/todo/items/:id/remove', methods=['DELETE'])
def todo_item_delete_handler ():
	pass
