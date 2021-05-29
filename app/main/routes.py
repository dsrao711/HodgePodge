from flask import render_template, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required

main = Blueprint('main', __name__)

@main.route("/")
def about():
    return render_template('landing_page.html')

@main.route("/home")
def home():
    current_user = {
        'username': "Yogesh Upadhyay"
    }
    return render_template('home.html' , current_user=current_user)

