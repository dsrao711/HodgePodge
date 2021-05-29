from flask import render_template, request, Blueprint,url_for
from flask_socketio import join_room, leave_room, send
from flask_login import login_user, current_user, logout_user, login_required
from app.users.forms import (RegistrationForm, LoginForm , UpdateAccountForm)
from app.models import User
from app import socketio

main = Blueprint('main', __name__)

@main.route("/")
def about():
    return render_template('landing_page.html')

@main.route("/home")
@login_required
def home():
    # friends = User.query.all()
    friends = User.query.with_entities(User.username)

    form = UpdateAccountForm()
    form.username.data = current_user.username
    form.email.data = current_user.email
    image_file = url_for('static', filename='/profile_pics/' + current_user.image_file)
    return render_template('home.html' , image_file=image_file ,form = form , friends = friends)


@socketio.on('message')
def handle_message(data):
    print(data)
    send(data, to=data['to'])

@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)
    send(room + ' has entered the room.', to=room)

@socketio.on('leave')
def on_leave(data):
    room = data['room']
    leave_room(room)
    send(room + ' has left the room.', to=room)