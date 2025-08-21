from flask import Flask
import os
from models import db
from routes import init_routes

def create_app():
    app = Flask(__name__)

    # Database setup
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'todo.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Init db
    db.init_app(app)

    # Register routes
    init_routes(app)

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
