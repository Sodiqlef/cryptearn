from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Payment(models.Model):
    user = models.OneToOneField(User, related_name='registration', on_delete=models.CASCADE, null=True)
    amount_paid = models.IntegerField(null = True)
    referral_username = models.CharField(max_length=255, null=True)
    date = models.DateTimeField(null=True, auto_now_add=True)
    approve = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'


class Earning(models.Model):
    user = models.OneToOneField(User, related_name='earning', on_delete=models.CASCADE, null=True)
    current = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user}'
    

