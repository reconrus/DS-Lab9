import json
from copy import deepcopy
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/chatDB"
mongo = PyMongo(app)

@app.route("/")
def home_page():
    posted_messages = mongo.db.messages.find({})
    socketio.emit('first launch', {'value': 12})
    return render_template("session.html",
        posted_messages=posted_messages)

@socketio.on('new message')
def handle_new_message(json_msg, methods=['GET', 'POST']):
    print('received my event: ' + str(json_msg))
    mongo.db.messages.insert(deepcopy(json_msg))
    socketio.emit('my response', json_msg)

@socketio.on('new connection')
def handle_new_connection(json_msg, methods=['GET', 'POST']):
    socketio.emit('my response', json_msg)

if __name__ == '__main__':
    socketio.run(app, debug=True)