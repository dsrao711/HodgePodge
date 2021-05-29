from os import path
from flask import Flask
from flask_socketio import SocketIO
from app.config import Config

socketio = SocketIO(path="/socket")

def register_extensions(app):

    # socket extension
    socketio.init_app(app)

def create_app(config_class=Config):
    app = Flask(
        __name__,
        static_folder="static"
    )
    
    app.config.from_object(Config)

    register_extensions(app)
    
    # registering blueprints
    from app.users.routes import users
    from app.main.routes import main
    
    app.register_blueprint(users)
    app.register_blueprint(main)
    
    return socketio, app