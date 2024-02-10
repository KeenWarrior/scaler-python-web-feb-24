import json

from django.http import HttpResponse, JsonResponse, HttpResponseServerError, HttpResponseNotFound
from django.http import HttpRequest
from .models import Payments

payments = [{
    "id": 1,
    "items": ["Mango", "Banana"],
    "total": 500,
    "status": "paid"
}, {
    "id": 2,
    "items": ["Apple", "Banana"],
    "total": 200,
    "status": "failed"
}]


# def get_all(request):
#     return JsonResponse({
#         "data": payments
#     })


def create_payment(request: HttpRequest):
    if request.method == "POST":
        body_json = json.loads(request.body)
        payment = Payments()
        payment.total = body_json["total"]
        payment.save()
        return JsonResponse(
            {
                "id": payment.id,
                "total":  payment.total,
                "status": payment.status
            }
        )


# def get_by_id(request, payment_id):
#     try:
#         if payment_id == 0:
#             raise Exception("No catch")
#         for payment in payments:
#             if payment["id"] == payment_id:
#                 return JsonResponse({
#                     "data": payment
#                 })
#
#         return JsonResponse({
#             "message": "No payment with id {}".format(payment_id)
#         }, status=404)
#
#     except Exception:
#         return JsonResponse({
#             "message": "Failed to fetch resource"
#         }, status=500)
#
# # def get_by_uuid(request, payment_id):
# #     return HttpResponse("payment with uuid: {}".format(payment_id))
# #
