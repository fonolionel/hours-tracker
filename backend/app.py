from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()

# Initialize the Flask app
app = Flask(__name__)

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # SQLite example

    db.init_app(app)

    # @app.route('/')
    # def index():
    #     return "ggg"
    
    # from route import register_routes
    # register_routes(app, db)

    migrate = Migrate(app, db)

    return app

