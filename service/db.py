import os
from pymongo import MongoClient

import todo

from models.user import user_model_init
from models.item import item_model_init

todo_db = None

def todo_mongo_init ():
	global todo_db

	client = MongoClient (todo.MONGO_URI)
	try:
		todo_db = client.todo
		print ("Mongo DB connected!")

		user_model_init (todo_db)
		item_model_init (todo_db)

	except:
		print ("Error connecting to Mongo DB")
