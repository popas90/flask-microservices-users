import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


# instantiate the db
db = SQLAlchemy()
# instantiate flask migrate
migrate = Migrate()
bcrypt = Bcrypt()


def create_app():

    # instantiate the app
    app = Flask(__name__)
    app.config['CORS_HEADERS'] = 'Content-Type'

    # enable CORS
    CORS(app)
    # CORS(app, resources={r"/users": {"origins": "http://localhost:3000"}})

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    from project.api.users import users_blueprint
    from project.api.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(users_blueprint)

    return app
