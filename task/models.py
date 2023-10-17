from django.db import models

class Transaction(models.Model):
    id = models.UUIDField(primary_key=True)
    date = models.DateField()
    type = models.TextField()
    description = models.TextField()
    debit = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    credit = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.description
