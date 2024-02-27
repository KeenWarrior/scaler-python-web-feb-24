from celery import Celery
from random_tasks.tasks import SimpleTask

app = Celery(
    'scaler_celery',
    broker='amqp://guest@localhost//'
)

simple_task = SimpleTask()
app.register_task(simple_task)

app.autodiscover_tasks(
    packages=["random_tasks"]
)




if __name__ == "__main__":
    args = ["worker", "--loglevel=DEBUG"]
    app.worker_main(argv=args)

