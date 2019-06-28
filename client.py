import socketio
import time

client = socketio.Client()

client.connect("http://18.228.137.154:5000")

def detected():
    """
    Envia a mensagem para o canal alert com objeto detectado.
    """

    client.emit("alert", "")

def batery(lvl):
    """
    Envia o nível de bateria para o canal batery
    """

    client.emit("batery", lvl)


def disconnect_from_server():
    """
    Desconecta do servidor
    """

    client.disconnect()


def wait():
    """
    Espera x segundos após a resposta da primeira para enviar a próxima
    """

    time.sleep(2)

@client.on('connect')
def on_connect():
    print("Conectei")


detected()
wait()
batery(20)
wait()
disconnect_from_server()

@client.on('disconnect')
def disconnect():
    print("Desconectei")