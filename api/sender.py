import pika
import os
import json


class Sender(object):
    """
    Classe responsável por enviar a mensagem
    para a fila de mensagens.
    """

    def __init__(self, data="Olaa mundo!"):
        """
        Construtor
        """

        self.data = data

        self.connect()
        self.send()
        self.close_connection()

    def connect(self):
        """
        Faz a conecção com o servidor do RabbitMQ
        """

        # IP da máquina que irá fazer as conecções
        IP = "localhost"

        # Estabelecer conecção com o servidor do RABBITMQ
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=IP))
        self.channel = self.connection.channel()

        # Criar a fila de mensagens, se ela não existir as mensagens serão descartadas.
        self.channel.queue_declare(queue='message_queue')

    def send(self):
        """
        Envia a mensagem para a fila de mensagens
        """

        self.channel.basic_publish(
            exchange='',
            routing_key='message_queue',
            body=json.dumps(self.data)
        )

        print(" [x] Sent 'Hello World!'")

    def close_connection(self):
        """
        Fecha a conecção
        """

        self.connection.close()