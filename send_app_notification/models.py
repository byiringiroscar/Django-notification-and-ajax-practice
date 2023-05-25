from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Notify(models.Model):
    notify_detail = models.TextField()
    read_by_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    status = models.BooleanField()
