from flask import Flask, jsonify, request
from exceptions import APIException
from sender import Sender
from http import HTTPStatus

app = Flask(__name__)

@app.route("/send_message/", methods=['POST'])
def message_received():
    """
    RECEPTOR
    Recebe a mensagem por meio de requisições
    HTTP do servidor de eletrônica e envia para
    o aplicativo por meio do evento 'message'.
    """

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

    Sender(data)

    return jsonify(data)


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
	  app.run(debug=True, host='0.0.0.0', port=3000)