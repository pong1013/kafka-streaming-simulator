import os
import sys
from confluent_kafka import Producer
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.kafka_config import BROKER, TOPIC_3, PRODUCER_3

# Producer config
def create_producer(client_id):
    return Producer({
        'bootstrap.servers': BROKER,
        'client.id': client_id,
    })

producer = create_producer(PRODUCER_3)

# Sand message to topic
def send_message(producer, topic, message):
    try:
        producer.produce(topic, key=message['key'], value=message['value'])
        producer.poll(0)
        print(f'Message sent to {topic}: {message}')
    except Exception as e:
        print(f'Failed to send message: {e}')

def get_random_number():
    return round(time.time() * 1000) % 1000

def create_message(num, partition=0):
    return {
        'key': f'key-{num}',
        'value': f'value-{num}-{time.strftime("%Y-%m-%dT%H:%M:%S")}',
        'partition': partition
    }

def main():
    topic = TOPIC_3
    try:
        while True:
            message = create_message(get_random_number())
            send_message(producer, topic, message)
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        producer.flush()

if __name__ == '__main__':
    main()
