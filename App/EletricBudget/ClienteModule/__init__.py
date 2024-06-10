from flask import Blueprint, request, session
from flask import redirect, render_template 
# from forms import ClienteLoginForm, ClienteRegisterForm, ClienteEditForm, ClienteScanStore
# from models import db, Cliente, bcrypt
from flask_login import login_user, logout_user, current_user 

ClienteModule = Blueprint("ClienteModule", __name__)

# @ClienteModule.route('/budgetList')
# def index():
#     return render_template('BudgetList.html', title='Login')

# @ClienteModule.route('/budgetAdd')
# def doLogin():
#     print("hello")
#     return render_template('LoginUser.html', title='Login')

# @ClienteModule.route('/budgetEdit')
# def doRegister():
#     print("hello")
#     return render_template('RegisterUser.html', title='Login')
