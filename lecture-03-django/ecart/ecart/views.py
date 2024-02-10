from django.http import HttpResponse, HttpRequest


def say_hello(request: HttpRequest):
    return HttpResponse("Hello from Scaler")
