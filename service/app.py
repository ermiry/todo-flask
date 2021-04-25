from flask import Flask

import db
import todo
import version

from controllers.service import todo_service_init
from controllers.users import todo_users_init

from routes.items import items
from routes.service import service
from routes.users import users

app = Flask (__name__)

app.config["JWT_ALGORITHM"] = "RS256"
with open (todo.PRIV_KEY, "r") as file:
    app.config["PRIV_KEY"] = file.read ()
with open (todo.PUB_KEY, "r") as file:
    app.config["PUB_KEY"] = file.read ()

app.register_blueprint (items)
app.register_blueprint (service)
app.register_blueprint (users)

if __name__ == '__main__':
	version.todo_version_print_full ()

	todo.todo_config ()
	
	db.todo_mongo_init ()

	todo_service_init (app)
	todo_users_init (app)

	app.run (debug=True, host="0.0.0.0", port=todo.PORT)
