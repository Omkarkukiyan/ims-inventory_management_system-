from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate


app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SECRET_KEY']='6c74c78d9c64456d862c43d2044d82cf'
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy(app)
bcrypt = Bcrypt()
bcrypt.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'main.login'
migrate = Migrate(app, db)


from app.models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from app.main.routes import main
from app.products.routes import product_blueprint
from app.locations.routes import location_blueprint
from app.product_movements.routes import movement_blueprint

app.register_blueprint(main)
app.register_blueprint(product_blueprint)
app.register_blueprint(location_blueprint)
app.register_blueprint(movement_blueprint)

