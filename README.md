## Servidor SmartWay

### Instalação

1) RabbitMQ

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install erlang
sudo apt-get install rabbitmq-server
sudo systemctl status rabbitmq-server
sudo systemctl enable rabbitmq-server
sudo systemctl start rabbitmq-server
```

Verificar se ta tudo ok

```
rabbitmqctl status
```