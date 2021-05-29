from flask import render_template, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from app.users.forms import (RegistrationForm, LoginForm)

main = Blueprint('main', __name__)

@main.route("/")
def about():
    return render_template('landing_page.html')

@main.route("/home")
@login_required
def home():
    form = RegistrationForm()
    form.username.data = current_user.username
    return render_template('home.html' , current_user=current_user)

