from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def hello():
	"""
	Endpoint para pegar o resultado
	da detecção de faixa de pedestre.
	"""

	return "Hello World"


if __name__ == '__main__':
	socketio.run(app, '127.0.0.1', 3000)