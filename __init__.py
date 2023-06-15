from flask import Flask
from app.config import Config
from app.extensions import db


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)
    db.init_app(app)

    from app.api.routes import bp as api_bp
    app.register_blueprint(api_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()