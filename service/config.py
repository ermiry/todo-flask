import os
from pymongo import MongoClient

db = None

def mongo ():
	global db

	client = MongoClient (os.environ.get ("MONGO_URI"))
	try:
		db = client.todo
		print ("Mongodb connected!")

	except:
		print ("Error connecting to Mongodb (Authentication Failed)")