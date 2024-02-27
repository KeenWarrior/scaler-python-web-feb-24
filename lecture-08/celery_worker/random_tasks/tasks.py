import celery
from celery import shared_task


@shared_task(name="say_hello")
def say_hello(name="BOB"):
    print("Hello {}".format(name))


@shared_task(name="say_bye")
def say_bye(name):
    print("Bye {}".format(name))


class SimpleTask(celery.Task):
    name = "simple_task"

    def run(self, param1, param2):
        print("We did work here")
        print(param1)
        print(param2)



