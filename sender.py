import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()      # factory, returns BlockingChannel

print(type(channel))

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body="Hello world! again")

print(" [x] Sent 'Hello World!'")

connection.close()

