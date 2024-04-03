import random
import time

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:29092')
for _ in range(100):
    value = '{"hello": "' + str(random.randint(1, 100)) + '"}'
    producer.send('test', value.encode())
    time.sleep(random.randint(1, 5))