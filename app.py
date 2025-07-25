import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from werkzeug.middleware.proxy_fix import ProxyFix
from sqlalchemy.orm import DeclarativeBase

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class Base(DeclarativeBase):
    pass

# Initialize extensions
db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "postgresql://user:password@localhost/raices_vivas")
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_recycle": 300,
        "pool_pre_ping": True,
    }
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # Proxy fix for URL generation
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
    
    # Initialize extensions
    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    login_manager.login_message = 'Por favor inicia sesión para acceder a esta página.'
    login_manager.login_message_category = 'info'
    
    return app

app = create_app()

with app.app_context():
    import models
    import routes
    db.create_all()
    logging.info("Database tables created")
    # Initialize sample data
    routes.create_sample_data()
