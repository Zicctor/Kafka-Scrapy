import unittest
from confluent_kafka import Consumer, KafkaError, Producer
import socket
import time

class TestKafkaProducer(unittest.TestCase):
    def setUp(self):
        self.kafka_broker = 'localhost:9092'
        self.kafka_topic = ''

        # Configure producer
        self.producer = Producer({
            'bootstrap.servers': self.kafka_broker,
            'client.id': socket.gethostname()
        })

        # Configure consumer
        self.consumer = Consumer({
            'bootstrap.servers': self.kafka_broker,
            'group.id': 'test_group',
            'auto.offset.reset': 'earliest'
        })
        self.consumer.subscribe([self.kafka_topic])

    def test_produce_and_consume(self):
        test_message = 'Hello, Kafka!'

        # Produce message
        self.producer.produce(self.kafka_topic, value=test_message)
        self.producer.flush()

        # Consume message
        msg = None
        start_time = time.time()
        while time.time() - start_time < 10:
            msg = self.consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break

            if msg.value().decode('utf-8') == test_message:
                break

        self.assertIsNotNone(msg, "No message received from Kafka")
        self.assertEqual(msg.value().decode('utf-8'), test_message, "The message received from Kafka does not match the produced message")

    def tearDown(self):
        self.consumer.close()

if __name__ == '__main__':
    unittest.main()
