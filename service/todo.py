import os

from runtime import *

RUNTIME = runtime_from_string (os.environ.get ("RUNTIME"))

PORT = int (os.environ.get ("PORT"))

MONGO_APP_NAME = os.environ.get ("MONGO_APP_NAME")
MONGO_DB = os.environ.get ("MONGO_DB")
MONGO_URI = os.environ.get ("MONGO_URI")

PRIV_KEY = os.environ.get ("PRIV_KEY")
PUB_KEY = os.environ.get ("PUB_KEY")

ENABLE_USERS_ROUTES = os.environ.get ("ENABLE_USERS_ROUTES")
if (ENABLE_USERS_ROUTES == "TRUE"):
	ENABLE_USERS_ROUTES = True
else:
	ENABLE_USERS_ROUTES = False

def todo_config ():
	print ("RUNTIME: ", runtime_to_string (RUNTIME))

	print ("PORT: ", PORT)

	print ("MONGO_APP_NAME: ", MONGO_APP_NAME)
	print ("MONGO_DB: ", MONGO_DB)
	print ("MONGO_URI: ", MONGO_URI)

	print ("PRIV_KEY: ", PRIV_KEY)
	print ("PUB_KEY: ", PUB_KEY)

	print ("ENABLE_USERS_ROUTES: ", ENABLE_USERS_ROUTES)
