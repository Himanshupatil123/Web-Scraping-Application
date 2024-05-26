from django.db import models

# Create your models here.

class WishList(models.Model):
    name=models.CharField(max_length=20)
    email_id=models.CharField(max_length=100)
    product_name=models.CharField(max_length=400)
    alert_price=models.IntegerField()
    date=models.DateField(null=True,blank=True)