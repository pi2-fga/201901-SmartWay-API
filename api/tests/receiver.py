import pika
import json

IP = "localhost"

connection = pika.BlockingConnection(pika.ConnectionParameters(host=IP))
channel = connection.channel()

channel.queue_declare(queue='message_queue')

def callback(ch, method, properties, body):
    body = json.loads(body.decode('utf-8'))
    print(" [x] Objeto encontrado: Distância = %s e Posição = %s" % (body['distance'], body['direction']))

channel.basic_consume(
    queue='message_queue',
    auto_ack=True,
    on_message_callback=callback
)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()