from flask import Flask, render_template
from app.models import db, User

def register_blueprints(app):
    from app.home import home as home_blueprint
    from app.auth import auth as auth_blueprint

    app.register_blueprint(home_blueprint)
    app.register_blueprint(auth_blueprint)

def initialize_extensions(app):
    from flask_migrate import Migrate

    db.init_app(app)
    Migrate(app, db)

def register_errorhandlers(app):
    # 400 - Bad Request
    @app.errorhandler(400)
    def bad_request(error):
        return render_template('errors/400.html', error=error)

    # 404 - Page Not Found
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', error=error)
    
    # 405 - Method Not Allowed
    @app.errorhandler(405)
    def method_not_allowed(error):
        return dict(error=error, status_code=405)

    # 500 - Internal Server Error
    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html', error=error)
    
# add cli tests commands
def register_tests_commands(app):
    @app.cli.command()
    def test():
        '''Run unit tests'''
        import unittest
        tests = unittest.TestLoader().discover('tests')
        unittest.TextTestRunner(verbosity=2).run(tests)

# register shell context processor
def register_shell_context_processor(app):
    @app.shell_context_processor
    def shell_context():
        return dict(db=db, User=User)

# application factory function
def create_app(config_name='development'):
    app = Flask(__name__)

    from config import config
    config_object = config[config_name]
    app.config.from_object(config_object)
    
    # initialize extensions
    initialize_extensions(app)
    # register blueprints
    register_blueprints(app)
    # register errorhandlers
    register_errorhandlers(app)
    # register tests commands
    register_tests_commands(app)
    # register shell context
    register_shell_context_processor(app)

    return app

