from flask import render_template, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required

from app.users.forms import RegistrationForm

main = Blueprint('main', __name__)

@main.route("/")
def about():
    return render_template('landing_page.html')


@main.route("/home")
def home():
    form = RegistrationForm()
    form.username.data = current_user.username
    
    return render_template('home.html' , form = form )

