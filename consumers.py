from kafka import KafkaConsumer

consumer = KafkaConsumer('msg_broker', auto_offset_reset='earliest')
for msg in consumer:
    print(msg)
