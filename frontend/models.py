from django.db import models

class Transaction(models.Model):
    amount = models.FloatField()
    age = models.IntegerField()
    is_fraud = models.BooleanField(default=False)
    # Add other fields as needed

    def __str__(self):
        return f"Transaction {self.id}"