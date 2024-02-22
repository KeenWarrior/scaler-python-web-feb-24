from celery import Celery

app = Celery(
    'scaler_celery',
    broker='amqp://guest@localhost//'
)

app.send_task("say_hello", args=["Anuj"])
app.send_task("say_hello", kwargs={
    "name": "Ravi"
})
