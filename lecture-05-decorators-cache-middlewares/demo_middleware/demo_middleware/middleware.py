from django.core.handlers.wsgi import WSGIRequest


def DemoMiddleware(get_response):
    print("Setup logic")

    def wrapped(request):
        print("DemoMiddleware: This will happen first")
        response = get_response(request)
        print("DemoMiddleware: This will happen later")
        return response

    return wrapped







# class DemoMiddleware:
#
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request: WSGIRequest):
#
#         print("DemoMiddleware: This will happen first")
#
#         response = self.get_response(request)
#         print("DemoMiddleware: This will happen later")
#         return response
#
#
# class AnotherMiddleware:
#
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request: WSGIRequest):
#         print("AnotherMiddleware: This will happen first")
#
#         response = self.get_response(request)
#         print("AnotherMiddleware: This will happen later")
#         return response
#
#
