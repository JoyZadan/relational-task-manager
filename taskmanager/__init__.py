"""
imports os, Flask and SQLAlchemy
imports env to use hidden environment variables
but only import 'env' if the os can find existing file path
for the env.py file to avoid Heroku deployment error
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env # noqa


# creates an instance of the imported Flask() class
# specifies app config variables
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

# creates an instance of the SQLAlchemy() class
# to be assigned to a variable 'db' and
# set to the instance of Flask 'app'
db = SQLAlchemy(app)

# from taskmanager package, import 'routes' file
from taskmanager import routes # noqa
