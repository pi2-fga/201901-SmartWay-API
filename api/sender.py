from constants import IP
import pika
import os
import json


class Sender(object):
    """
    Classe responsável por enviar a mensagem
    para a fila de mensagens.
    """

    def __init__(self, data):
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

        # Estabelecer conecção com o servidor do RABBITMQ
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=IP))
        self.channel = self.connection.channel()

        # Criar a fila de mensagens, se ela não existir as mensagens serão descartadas.
        self.channel.queue_declare(queue='message_queue', durable=True)

        # Cria o gerenciador de mensagens, pega as mensagens e insere nas filas
        self.channel.exchange_declare(exchange='direct_log', exchange_type='direct')

    def send(self):
        """
        Envia a mensagem para a fila de mensagens
        """

        self.channel.basic_publish(
            exchange='direct_log',
            routing_key='message_queue',
            body=json.dumps(self.data)
        )

    def close_connection(self):
        """
        Fecha a conecção
        """

        self.connection.close()