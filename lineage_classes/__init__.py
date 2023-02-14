import os

from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI = "sqlite:///classes.sqlite",
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
    )
    app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    
    from .model import db, init_db_command
    db.init_app(app)
    with app.app_context():
        app.cli.add_command(init_db_command)
        
    from . import routes
    app.register_blueprint(routes.bp)
        
        

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app