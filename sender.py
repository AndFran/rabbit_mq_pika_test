import pika

message = "This is a test message"

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()  # factory, returns BlockingChannel

print(type(channel))

channel.queue_declare(queue='test_queue')

channel.basic_publish(exchange='',
                      routing_key='test_queue',
                      body=message)
print("Sent '{}'".format(message))

connection.close()
