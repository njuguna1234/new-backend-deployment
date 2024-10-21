from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.user_routes import user_bp
    from .routes.artwork_routes import artwork_bp
    from .routes.review_routes import review_bp
    from .routes.purchase_routes import purchase_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(artwork_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(purchase_bp)

    return app
