import pika
import config
import time
import json


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue=config.qname)

for count in range(100):
    msg = {"count": count, "time": time.time()}
    channel.basic_publish(exchange='',
                          routing_key=config.qname,
                          body=json.dumps(msg))
    time.sleep(4)
print(" [x] Sent 'Message from Producer'")
connection.close()
