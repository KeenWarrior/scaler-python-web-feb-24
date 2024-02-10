from django.db import models

# Create your models here.
from django.db import models


class BaseModel(models.Model):
    pass


class PaymentStatus(models.TextChoices):
    PAID = "PAID"
    PENDING = "PENDING"
    FAILED = "FAILED"


class Payments(models.Model):
    id = models.IntegerField(primary_key=True)
    total = models.IntegerField(),
    status = models.CharField(choices=PaymentStatus.choices, max_length=50, default=PaymentStatus.PENDING)
