from flask import Blueprint, request, session
from flask import redirect, render_template 
# from forms import ClienteLoginForm, ClienteRegisterForm, ClienteEditForm, ClienteScanStore
# from models import db, Cliente, bcrypt
from flask_login import login_user, logout_user, current_user 

ServiceModule = Blueprint("ServiceModule", __name__)

@ServiceModule.route('/serviceList')
def seeServiceList():
    return render_template('ServiceList.html', title='Login')

# @ServiceModule.route('/budgetAdd')
# def doLogin():
#     print("hello")
#     return render_template('LoginUser.html', title='Login')

# @ServiceModule.route('/budgetEdit')
# def doRegister():
#     print("hello")
#     return render_template('RegisterUser.html', title='Login')