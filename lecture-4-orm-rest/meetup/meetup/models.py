from django.db import models


class BaseClass(models.Model):
    class Meta:
        abstract=True


class User(BaseClass):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)


class Group(BaseClass):
    name = models.CharField(max_length=255)
    admins = models.ManyToManyField(User, related_name="groups_with_admin")
    participants = models.ManyToManyField(User, related_name="groups", default=[])


class Event(BaseClass):
    name = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    start_date = models.DateField()
    rsvp = models.ManyToManyField(User, related_name="rsvp")




