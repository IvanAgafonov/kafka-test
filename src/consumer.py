import json

from kafka import KafkaConsumer

consumer = KafkaConsumer('test', bootstrap_servers='localhost:29092')
for msg in consumer:
    print(msg)
    obj = json.loads(msg.value.decode())
    print(obj['hello'])