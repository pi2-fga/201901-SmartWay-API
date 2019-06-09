from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def connect():
    print('Client connected')

@socketio.on('alert')
def handle_message(message):
    print('recceived message: ' + str(message))
    emit('mobile', message, broadcast=True)

@socketio.on('disconnect')
def disconnect():
    print("Client disconnected")

if __name__ == '__main__':
    socketio.run(app, debug=False, host="0.0.0.0", port="5000")