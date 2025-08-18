from django.db import models

class Card(models.Model):
    uid = models.CharField(max_length=32, unique=True) 
    balance = models.IntegerField(default=0)
    status = models.CharField(max_length=10, default="activa")
    register = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

class Transaction(models.Model):
    card = models.ForeignKey(Card, on_delete=models.PROTECT)
    type = models.CharField(
        max_length=15,
        choices=[
            ('transaction', 'Transaction'),
            ('use', 'Use'),
        ],
        default='transaction'
    )
    mount = models.PositiveBigIntegerField(default=0)
    balance_before = models.PositiveBigIntegerField(default=0)
    balance_after = models.PositiveBigIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
