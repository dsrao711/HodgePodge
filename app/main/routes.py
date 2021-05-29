from flask import render_template, request, Blueprint


main = Blueprint('main', __name__)

@main.route("/")
def about():
    chats = ["Goblu", "Gobli", "Chinnu", "Gapuli"]*56
    return render_template('chat.html',  chats=chats)

