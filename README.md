## Servidor SmartWay

Para testar execute os comandos abaixo:

```
docker-compose up

RECEPTORES:
  $ node api/tests/receiver.js
  $ python3 api/tests/receiver.py

TRANSMISSOR:
  $ python3 api/tests/client_eletronic.py
```

### Como funciona

**1)** Inserir o código do arquivo ```client_eletronic``` no
servidor que se encontra no seu raspberryPI para envio
de dados para o nosso servidor.

**2)** Insira um dos receivers no código que irá receber as notificações
do servidor do raspberryPI, por exemplo, no seu site ou aplicativo.

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

### Dependências

1) docker
2) docker-compose
3) node, npm
4) python3