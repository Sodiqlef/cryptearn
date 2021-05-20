from django.db import models

# Create your models here.

class WalletID(models.Model):
    wallet_id = models.CharField(max_length=200)
