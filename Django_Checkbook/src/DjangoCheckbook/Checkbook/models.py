from django.db import models


# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2)

    Accounts = models.Manager

    # Allows returning references to a specific account
    # as the owner's name isn' the primary key
    def __str__(self):
        return self.first_name + ' ' + self.last_name
