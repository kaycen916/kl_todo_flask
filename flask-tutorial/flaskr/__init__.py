import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True) #creates the Flask instance
    app.config.from_mapping(
        SECRET_KEY='dev', #keep data safe
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True) #overrides the default configuration with values taken from the config.py file
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from . import db
    db.init_app(app)
    
    # Import and register the blueprint from the factory 
    # using app.register_blueprint().
    from . import auth
    app.register_blueprint(auth.bp)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, world!'
    return app