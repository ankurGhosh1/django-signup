from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.
class UserExtended(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.IntegerField()

    def __str__(self):
        return self.phone