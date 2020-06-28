from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

application = Flask(__name__)
application.config.from_object(Config)

db = SQLAlchemy(application)
mirgrate = Migrate(application, db)
login = LoginManager(application)
login.login_view = 'login'

application.config.update(
        DEBUG=True)

from app import routes, models




'''
GET
POST - u send some parameters.
DELETE
PUT
PATCH


flask db init
flask db migrate
flask upgrade


db.session.add(u)
db.session.commit()
'''

