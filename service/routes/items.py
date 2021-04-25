from flask import Blueprint, jsonify, request, make_response

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
		return make_response (result, 200, {"Content-Type": "application/json"})

	else:
		return jsonify ({
			"items": []
		}), 200

# POST /api/todo/items/register
# a user has requested to create a new item
@items.route ('/api/todo/items', methods=['POST'])
@controllers.service.token_required
def todo_item_create_handler (decoded_user):
	result = controllers.items.todo_item_create (decoded_user, request)

	if result == TODO_ERROR_NONE:
		return jsonify ({"msg": "Created a new item!"}), 200

	else:
		return todo_error_send_response (result)

# GET /api/todo/items/:id/info
# returns information about an existing item that belongs to a user
@items.route ('/api/todo/items/<item_id>/info', methods=['GET'])
@controllers.service.token_required
def items_login_handler (decoded_user, item_id):
	result = controllers.items.todo_item_get_by_id_and_user_to_json (
		decoded_user, item_id
	)

	if (result is not None):
		return make_response (result, 200, {"Content-Type": "application/json"})

	else:
		return jsonify ({"error": "Item not found"}), 404

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
