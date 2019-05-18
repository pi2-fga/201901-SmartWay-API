from flask import Flask, jsonify, request
from exceptions import APIException
from http import HTTPStatus
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('message')
def message_send(data):
	"""
	TRANSMISSOR
	Recebe a mensagem vindo do client
	criado pelo pessoal de eletronica.
	"""

	print("ENTREII TRANSMISSOR")
	print(data)

	# Envia a mensagem para o cliente mobile.
	emit('mobile', data)

@app.route("/send_message/", methods=['POST'])
def message_received(message):
	"""
	RECEPTOR
	Recebe a mensagem por meio de requisições
	HTTP do servidor de eletrônica e envia para
	o aplicativo por meio do evento 'message'.
	"""

	print("ENTREII RECEPTOR")

	data = request.get_json()

	if not data:
		raise APIException(
            "Os dados foram informados da maneira errada.",
            status_code=HTTPStatus.BAD_REQUEST
        )

	if "direction" not in data.keys() or "distance" not in data.keys():
		raise APIException(
            "Insira a direção e a distancia do objeto.",
            status_code=HTTPStatus.BAD_REQUEST
        )

	emit('message', data)

	return jsonify(data)


@app.route("/")
def client_mobile():
	"""
	Teste simulando um cliente JS
	"""

	return open("tests/client_mobile.html").read()


@app.errorhandler(APIException)
def handle_invalid_data(error):
    """
    Faz com que a requisição retorne
    uma exceção em formato JSON caso ocorra.
    """

    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == '__main__':
	socketio.run(app, debug=True, host='0.0.0.0', port=3000)