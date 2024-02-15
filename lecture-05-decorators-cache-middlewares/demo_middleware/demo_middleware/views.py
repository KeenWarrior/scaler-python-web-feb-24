from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from datetime import datetime
from django.core.cache import cache
from json import dumps

from throttle.decorators import throttle


class GenericView(View):

    @method_decorator(throttle(zone="default"))
    def get(self, request):
        return HttpResponse(str(datetime.now()))

