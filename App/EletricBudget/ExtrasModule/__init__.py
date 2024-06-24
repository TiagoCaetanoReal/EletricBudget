from flask import Blueprint, request, session
from flask import redirect, render_template 
# from forms import ClienteLoginForm, ClienteRegisterForm, ClienteEditForm, ClienteScanStore
# from models import db, Cliente, bcrypt
from flask_login import login_user, logout_user, current_user 

ExtrasModule = Blueprint("ExtrasModule", __name__)

@ExtrasModule.route('/extrasList')
def seeExtrasList():
    return render_template('Extras.html', title='Extras')