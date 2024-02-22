import pika

params = pika.ConnectionParameters(

)

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare("scaler_queue")
channel.exchange_declare("scaler_exchange")

channel.queue_bind("scaler_queue","scaler_exchange")

for method, properties, body in channel.consume("scaler_queue"):
    print(body, properties)
    channel.basic_ack(method.delivery_tag)


connection.close()

