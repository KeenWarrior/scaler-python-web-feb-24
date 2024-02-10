from django.urls import path
from .views import get_all, get_by_id, get_by_uuid


urlpatterns = [
    path('', get_all),
    path('<str:payment_id>', get_by_uuid),
    path('<int:payment_id>', get_by_id),
]
