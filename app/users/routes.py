from flask import render_template, request, Blueprint


users = Blueprint('users', __name__)

@users.route("/")
def about():
    return render_template('home.html')