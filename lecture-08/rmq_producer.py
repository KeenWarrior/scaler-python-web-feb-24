import datetime

import pika

params = pika.ConnectionParameters(

)

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare("scaler_queue")
channel.exchange_declare("scaler_exchange")

channel.queue_bind("scaler_queue","scaler_exchange")

time = str(datetime.datetime.now())

channel.basic_publish(
    exchange="scaler_exchange",
    routing_key="scaler_queue",
    body=bytes(f"Hello from scaler at time : {time}", "utf-8")
)

connection.close()

