from flask import Flask
from app.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.routes import main
    from app.spectacles.routes import spectacles
    from app.galerie.routes import galerie

    app.register_blueprint(main)
    app.register_blueprint(spectacles)
    app.register_blueprint(galerie)

    return app
