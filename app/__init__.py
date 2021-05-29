from os import path
from flask import Flask
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

mail = Mail()
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
socketio = SocketIO(path="/socket")

def register_extensions(app):
    # socket extension
    socketio.init_app(app)

    # bcrypt extension
    bcrypt.init_app(app)

    # initializing login manager extension
    login_manager.init_app(app)
    login_manager.login_view = 'users.login'
    login_manager.login_message_category = 'info'

    # mail extension
    mail.init_app(app)

def db_init(app):
    # initialize database
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(
        __name__,
        static_folder="static"
    )
    
    app.config.from_object(Config)

    # registering extensions
    register_extensions(app)

    # initialize database
    # db_init(app)
    
    # registering blueprints
    from app.users.routes import users
    from app.main.routes import main
    
    app.register_blueprint(users)
    app.register_blueprint(main)
    
    return socketio, app
