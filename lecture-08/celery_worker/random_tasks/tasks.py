from celery import shared_task


@shared_task(name="say_hello")
def say_hello(name="BOB"):
    print("Hello {}".format(name))


@shared_task(name="say_bye")
def say_bye(name):
    print("Bye {}".format(name))

