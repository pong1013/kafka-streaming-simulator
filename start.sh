#!/bin/bash

# create kafka topics
python3 src/topics/kafka_topics.py

# Run producers
python3 src/producers/producer_1.py
python3 src/producers/producer_2.py
python3 src/producers/producer_3.py

# Run consumers
python3 src/consumers/consumer_1.py
python3 src/consumers/consumer_2.py
python3 src/consumers/consumer_3.py
