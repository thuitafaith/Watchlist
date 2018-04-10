from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap
from config import config_options

#initializing application
app = Flask(__name__,instance_relative_config = True)
# setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Initializing Flask Extensions
bootstrap = Bootstrap(app)
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    # creating the app configurations
    app.config.from_object(config_options[config_name])

    #initializing flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)

    #registering the Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # setting config
    from .requests import configure_request
    configure_request(app)

    return app
#from app import views
#from app import error
