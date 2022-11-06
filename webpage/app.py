import os
from flask import *
from flask_sqlalchemy import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)
from models import *
with app.app_context():
	db.create_all()

# Website routes.
from routes import *

# API endpoints.
from api import *

# AJAX endpoints.
from ajax import *
