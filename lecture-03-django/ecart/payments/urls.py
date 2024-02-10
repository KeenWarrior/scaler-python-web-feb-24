from django.urls import path
from .views import create_payment


urlpatterns = [
    path('', create_payment),
    # path('<int:payment_id>', get_by_id),
]
