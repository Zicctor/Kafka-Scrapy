from confluent_kafka import Producer

conf = {
    'bootstrap.servers': 'localhost:9092',  # Replace with your Kafka broker
}

producer = Producer(**conf)

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def send_message(topic, message):
    producer.produce(topic, message.encode('utf-8'), callback=delivery_report)
    producer.flush()
