from http import HTTPStatus
import requests
import json

DATA = {
	  "direction": "esquerda",
	  "distance": "2 metros"
}


def send(data):
    """
    Envia os dados para o servidor
    de software.
    """

    url = "http://18.228.137.154:3000/send_message/"

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

    print(response.status_code)
    return True


if __name__ == '__main__':
    send(DATA)
