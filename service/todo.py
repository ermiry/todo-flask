import os

from runtime import *

RUNTIME = RUNTIME_TYPE_NONE

PORT = 5000

MONGO_APP_NAME = None
MONGO_DB = None
MONGO_URI = None

PRIV_KEY = None
PUB_KEY = None

def todo_init ():
	global RUNTIME

	global PORT

	global MONGO_APP_NAME
	global MONGO_DB
	global MONGO_URI

	global PRIV_KEY
	global PUB_KEY

	RUNTIME = runtime_from_string (os.environ.get ("RUNTIME"))

	PORT = int (os.environ.get ("PORT"))

	MONGO_APP_NAME = os.environ.get ("MONGO_APP_NAME")
	MONGO_DB = os.environ.get ("MONGO_DB")
	MONGO_URI = os.environ.get ("MONGO_URI")

	PRIV_KEY = os.environ.get ("PRIV_KEY")
	PUB_KEY = os.environ.get ("PUB_KEY")
