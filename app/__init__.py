from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from datetime import date
import logging
from logging.handlers import TimedRotatingFileHandler
import os

application = Flask(__name__)
application.config.from_object(Config)

UPLOAD_FOLDER = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(application)
mirgrate = Migrate(application, db)
login = LoginManager(application)
login.login_view = 'login'
application.config.update(
        DEBUG=True)

currentDate = date.today()
file_handler = TimedRotatingFileHandler(
    filename='app/logs/query.' + str(currentDate) + '.log', when='midnight', backupCount=30 )

# formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# file_handler.setFormatter(formatter)
# logger = logging.getLogger('query')
# logger.addHandler(file_handler)
# logger.setLevel(logging.DEBUG)



from app.errors import bp as errors_bp
application.register_blueprint(errors_bp)

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

