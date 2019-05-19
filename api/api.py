from flask import Flask, jsonify, request
from cnn import CrosswalkCNN
from exceptions import APIException
from sender import Sender
from http import HTTPStatus
from werkzeug.utils import secure_filename
import os
import shutil

UPLOAD_FOLDER = "img"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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


def allowed_file(filename):
    """
    Verifica se o arquivo tem a extensão
    permitida para a inserção.
    """

    return "." in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/detect_crosswalk/", methods=['POST'])
def detect_crosswalk():
    """
    Endpoint para detecção de faixas de pedestre.
    """

    if request.method == "POST":
        if "file" not in request.files:
            raise APIException(
                "Imagem não encontrada.",
                status_code=HTTPStatus.BAD_REQUEST
            )

        img = request.files['file']

        if img.filename == '':
            raise APIException(
                "Nenhuma imagem selecionada.",
                status_code=HTTPStatus.BAD_REQUEST
            )

        try:
            os.mkdir("img")
        except Exception:
            pass

        if img and allowed_file(img.filename):
            filename = secure_filename(img.filename)
            img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            text, is_crosswalk = CrosswalkCNN.crosswalk_detector("./img/" + img.filename)

            shutil.rmtree("./img")

            return jsonify({
                "result": is_crosswalk,
                "message": text
            })

        raise APIException(
            "Extensão da imagem invalida.",
            status_code=HTTPStatus.BAD_REQUEST
        )


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
	  app.run(debug=False, host='0.0.0.0')