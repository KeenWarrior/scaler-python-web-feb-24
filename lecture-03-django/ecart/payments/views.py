from django.http import HttpResponse


def get_all(request):
    return HttpResponse("All payments")


def get_by_id(request, payment_id):
    return HttpResponse("payment with id: {}".format(payment_id))


def get_by_uuid(request, payment_id):
    return HttpResponse("payment with uuid: {}".format(payment_id))

