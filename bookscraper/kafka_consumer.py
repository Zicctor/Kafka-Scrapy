from confluent_kafka import Consumer
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'minhkhoivlu27@gmail.com'
    msg['To'] = 'svshirunai123@gmail.com'

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('minhkhoivlu27@gmail.com', 'lxsl eaer kdkq jnmk')  # Ensure no non-ASCII characters
        server.sendmail(msg['From'], [msg['To']], msg.as_string())

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'email_group',
    'auto.offset.reset': 'earliest',
}

consumer = Consumer(**conf)
consumer.subscribe(['email_topic'])

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(f"Consumer error: {msg.error()}")
        continue

    message_content = msg.value().decode('utf-8')
    print(f"Received message: {message_content}")

    if "has completed scraping" in message_content:
        send_email('Scrapy Job Completed', 'The scraping process has completed successfully, please check the database for data.')
        break  # Exit the loop after sending the completion email

consumer.close()
