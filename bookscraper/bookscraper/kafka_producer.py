from confluent_kafka import Producer
import socket

class KafkaProducer:
    def __init__(self, kafka_broker):
        self.producer = Producer({
            'bootstrap.servers': kafka_broker,
            'client.id': socket.gethostname()
        })

    def produce(self, topic, message):
        self.producer.produce(topic, value=message)
        self.producer.flush()
