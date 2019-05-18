from http import HTTPStatus
import requests
import json

DATA = {
	  "direction": "direita",
	  "distance": "2 metros"
}


def send(data):
    """
    Envia os dados para o servidor
    de software.
    """

    url = "http://0.0.0.0:3000/send_message/"

    header = {'Content-type': 'application/json'}

    response = requests.post(
        url,
        data=json.dumps(data),
        headers=header
    )

    if response.status_code == HTTPStatus.BAD_REQUEST:
        error = response.json()
        print("O FORMATO DOS DADOS ESTÃO SINTATICAMENTE INCORRETOS.")
        print(error.get('message', 'Erro desconhecido'))
        return False

    return True


if __name__ == '__main__':
    send(DATA)