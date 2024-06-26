from flask import Flask
from flask_login import LoginManager
from flask_babel import Babel
# from models import db, bcrypt, Cliente

from  AutenticationModule import AutenticationModule
from  BudgetModule import BudgetModule
from  ClienteModule import ClienteModule
from  ServiceModule import ServiceModule
from ExtrasModule import ExtrasModule
# from frontOffice.StoreClientModule import StoreClientModule

def create_app(config_filename):
	app = Flask(__name__)
	app.config.from_object(config_filename)
	
	# db.init_app(app)
	# bcrypt.init_app(app)

	# with app.app_context():
	# 	db.create_all()

	# login_manager = LoginManager()
	# login_manager.login_view = 'auth.login'
	# login_manager.init_app(app)

	# @login_manager.user_loader
	# def load_user(user_id):
	# 	return Cliente.query.get(int(user_id))

	app.register_blueprint(AutenticationModule)
	app.register_blueprint(BudgetModule)
	app.register_blueprint(ClienteModule)
	app.register_blueprint(ServiceModule)
	app.register_blueprint(ExtrasModule)
	# app.register_blueprint(StoreClientModule)

	babel = Babel(app)
	
	return app


if __name__ == "__main__":
	app = create_app("config.DevelopmentConfig")
	app.run(debug=True)