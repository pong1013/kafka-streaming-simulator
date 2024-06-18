from confluent_kafka import Consumer, KafkaException, KafkaError
import os
import sys
import pymysql
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.kafka_config import BROKER, Group_2, TOPIC_2

load_dotenv()

# mysql config
MYSQL_HOST = 'localhost'
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')

# kafka config
consumer_config = {
    'bootstrap.servers': BROKER,
    'group.id': Group_2,
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_config)
consumer.subscribe([TOPIC_2])

def insert_message(cursor, key, value, partition, offset):
    sql = "INSERT INTO topic_messages_2 (message_key, message_value, `partition`, `offset`) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (key, value, partition, offset))


def connect_to_mysql():
    return pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

def consume_messages():
    conn = connect_to_mysql()
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
                key = msg.key().decode('utf-8') if msg.key() else None
                value = msg.value().decode('utf-8') if msg.key() else None
                partition = msg.partition()
                offset = msg.offset()
                print(f'Received message: {msg.key().decode("utf-8")}: {msg.value().decode("utf-8")}')
                
                with conn.cursor() as cursor:
                    insert_message(cursor, key, value, partition, offset)
                conn.commit()
                    
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == '__main__':
    consume_messages()
