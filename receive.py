import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()  # factory, returns BlockingChannel

channel.queue_declare(queue='test_queue')


def callback(ch, method, properties, body):
    print("Received in callback: %r" % body)

channel.basic_consume(callback,
                      queue='test_queue',
                      no_ack=True)

print('Waiting for message. Press CTRL+C')
channel.start_consuming()

print("Finished")
