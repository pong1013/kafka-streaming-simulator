
import os
import sys
from confluent_kafka.admin import AdminClient, NewTopic


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.kafka_config import BROKER

def create_topic(topic_name, num_partitions, replication_factor=1):
    admin_client = AdminClient({'bootstrap.servers': BROKER})
    topic_list = [NewTopic(topic=topic_name, num_partitions=num_partitions, replication_factor=replication_factor)]
    
    create_new_topic = admin_client.create_topics(topic_list)
    
    for topic, create in create_new_topic.items():
        try:
            create.result()  # The result itself is None
            print(f"Topic {topic} created successfully")
        except Exception as e:
            print(f"Failed to create topic {topic}: {e}")

if __name__ == "__main__":
    topics = [
        {'topic': 'Sdorica-sunset-topic', 'partitions': 3},
        {'topic': 'Cytus2-topic', 'partitions': 3},
        {'topic': 'Deemo2-topic', 'partitions': 3},
    ]
    
    for topic in topics:
        create_topic(topic["topic"], topic["partitions"])
