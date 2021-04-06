from flask import Flask

import db
import todo
import version

from routes.items import items
from routes.service import service
from routes.users import users

app = Flask (__name__)
app.register_blueprint (items)
app.register_blueprint (service)
app.register_blueprint (users)

if __name__ == '__main__':
	version.todo_version_print_full ()

	todo.todo_init ()
	# db.todo_mongo_init ()

	app.run (debug=True, host="0.0.0.0", port=todo.PORT)
