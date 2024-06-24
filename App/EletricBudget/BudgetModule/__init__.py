from flask import Blueprint, request, session
from flask import redirect, render_template, url_for
# from forms import ClienteLoginForm, ClienteRegisterForm, ClienteEditForm, ClienteScanStore
# from models import db, Cliente, bcrypt
from flask_login import login_user, logout_user, current_user 

BudgetModule = Blueprint("BudgetModule", __name__)

@BudgetModule.route('/budgetList')
def seeBudgetList():
    return render_template('BudgetList.html', title='Budget List')

@BudgetModule.route('/budgetAdd')
def enterAddBudget():
    print("hello")
    return render_template('BudgetList.html', title='Login')

@BudgetModule.route('/budgetEdit')
def enterEditBudget():
    print("hello")
    return render_template('BudgetList.html', title='Login')