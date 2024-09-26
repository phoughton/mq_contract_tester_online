import config
import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue (idempotent operation)
channel.queue_declare(queue=config.qname)

# Publish a message to the queue
channel.basic_publish(exchange='',
                      routing_key=config.qname,
                      body='Hello, RabbitMQ!')

print(" [x] Sent 'Hello, RabbitMQ!'")

connection.close()
