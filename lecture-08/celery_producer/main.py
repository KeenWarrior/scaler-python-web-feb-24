from celery import Celery

app = Celery(
    'scaler_celery',
    broker='amqp://guest@localhost//'
)

app.send_task("simple_task", kwargs={
    "param1": "hello",
    "param2": "world"
})
