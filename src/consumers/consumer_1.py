from confluent_kafka import Consumer, KafkaException, KafkaError
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.kafka_config import BROKER, Group_1, TOPIC_1


consumer_config = {
    'bootstrap.servers': BROKER,
    'group.id': Group_1,
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_config)
consumer.subscribe([TOPIC_1])

def consume_messages():
    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f'End of partition reached {msg.topic()} [{msg.partition()}] at offset {msg.offset()}')
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                print(f'Received message: {msg.key().decode("utf-8")}: {msg.value().decode("utf-8")}')
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == '__main__':
    consume_messages()
