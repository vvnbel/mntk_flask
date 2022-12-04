from flask import Flask
from config import Cfg
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_avatars import Avatars

app = Flask(__name__)
avatars = Avatars(app)

app.config.from_object(Cfg)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'


from app import routes, models
