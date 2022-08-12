from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
for _ in range(100):
    # foobar topic 에 메시지를 전송 합니다.
    producer.send('msg_broker', b'some_message_bytes')

future = producer.send('foobar1', b'another_message')
result = future.get(timeout=60)
producer.flush()
producer.send('msg_broker', key=b'foo', value=b'bar')
producer.close()

# json 형태로 송부 합니다.
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer.send('fizzbuzz', {'foo': 'bar'})

# Serialize string keys
producer = KafkaProducer(key_serializer=str.encode)
producer.send('flipflap', key='ping', value=b'1234')

# Compress messages
producer = KafkaProducer(compression_type='gzip')
for i in range(1000):
    producer.send('foobar', b'msg %d' % i)