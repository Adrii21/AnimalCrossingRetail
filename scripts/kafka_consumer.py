from confluent_kafka import Consumer, KafkaException
from pymongo import MongoClient
import json

# Kafka consumer configuration
conf = {
    'bootstrap.servers': "localhost:9092",
    'group.id': "scraper_group",
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(**conf)
consumer.subscribe(['scraped-data'])

# MongoDB configuration
client = MongoClient('localhost', 27017)
db = client['products']
collection = db['items']

# Clean the collection before insert new data
collection.delete_many({})

# Kafka message consumer
def consume_messages():
    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    raise KafkaException(msg.error())
            item = json.loads(msg.value().decode('utf-8'))
            collection.insert_one(item)
            print(f"Item {item['name']} insertado en MongoDB")
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

consume_messages()
