## Servidor SmartWay

Para testar execute os comandos abaixo:

```
INSTALANDO OPENCV:
  $ sudo apt-get install python-opencv

RODAR O RABBITMQ:
  $ docker-compose up

ENTRAR NA PASTA DA API:
  $ cd api

RODAR O SERVIDOR (API):
  $ pip install -r requirements.txt
  $ gunicorn -b 0.0.0.0:3000 wsgi --reload --log-level DEBUG --workers 5 --daemon

RECEPTORES:
  $ node api/tests/receiver.js
  $ python3 api/tests/receiver.py

TRANSMISSOR:
  $ python3 api/tests/client_eletronic.py

RODAR O SERVIDOR WEBSOCKET:
  $ pip install -r requirements.txt
  $ python3 websocket.py
```

OBS: use o ```--daemon``` somente em produção para deixar o servidor em modo background.
OBS: O OpenCV não funciona em ambientes virtuais do python.

### Como funciona

**1)** Inserir o código do arquivo ```client_eletronic``` no
servidor que se encontra no seu raspberryPI para envio
de dados para o nosso servidor de fila de mensagens.

**2)** Insira um dos receivers no código que irá receber as notificações
do servidor do raspberryPI, por exemplo, no seu site ou aplicativo.

**3)**: No seu site ou aplicativo vc também pode consumir um dos nossos endpoints.

### Endpoints

**1)** /send_message/ - POST

Endpoint usado para enviar os dados do raspberry para
a fila de mensagens do servidor.

Entrada:

```
{
  "direction": "Direção em que se encontra o objeto.",
	"distance": "Distância do objeto encontrado."
}
```

Saída: N/A

Status:

* 200 - OK
* 400 - BAD REQUEST

**2)** /detect_crosswalk/ - POST

Endpoint para detecção de faixas de pedestre.

Entrada: Imagem

Saída: {
  "result": True OU False,
  "message": "É uma faixa de pedestre." OU "Não é uma faixa de pedestre."
}

Status:

* 200 - OK
* 400 - BAD REQUEST

![img](https://user-images.githubusercontent.com/14116020/57976637-441b5d00-79bb-11e9-822c-8cd0d6aa083e.png)

### Dependências

1) docker
2) docker-compose
3) node, npm
4) python3