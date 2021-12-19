from django.db import models
from accounts.models import Account


# Create your models here.

class MembersModels(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AlertModel(models.Model):
    location = models.CharField(max_length=100)
    river_level = models.CharField(max_length=100, blank=True, default = 0)
    members = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.location} - {self.river_level}'
