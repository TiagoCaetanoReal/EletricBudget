from flask import Blueprint, request, session
from flask import redirect, render_template 
# from forms import ClienteLoginForm, ClienteRegisterForm, ClienteEditForm, ClienteScanStore
# from models import db, Cliente, bcrypt
from flask_login import login_user, logout_user, current_user 

AutenticationModule = Blueprint("AutenticationModule", __name__)

@AutenticationModule.route('/')
def index():
    return redirect('/login')

@AutenticationModule.route('/login')
def doLogin():
    print("hello")
    return render_template('LoginUser.html', title='Login')

@AutenticationModule.route('/register')
def doRegister():
    print("hello")
    return render_template('LoginUser.html', title='Login')