#!/usr/bin/env node
// npm install amqplib

let amqp = require('amqplib/callback_api');

amqp.connect('amqp://localhost', function(error0, connection) {
    if (error0) throw error0;

    connection.createChannel(function(error1, channel) {
        if (error1) throw error1;

        let queue = 'message_queue';

        channel.assertQueue(queue, { durable: false });

        console.log(" [*] Esperando a mensagem em %s. Aperte CTRL+C para sair", queue);

        channel.consume(queue, function(msg) {
            let body = JSON.parse(msg.content);
            console.log(" [x] Objeto encontrado: Distância = %s e Posição = %s", body.distance, body.direction)
        });
    });
});