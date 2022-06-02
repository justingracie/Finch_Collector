from email.policy import default
from django.db import models

# Create your models here.
class Coin(models.Model):
    type = models.TextField(max_length=125)
    year = models.CharField(max_length=20)
    img = models.CharField(max_length=400, default='./images/default.jpg')
    value = models.CharField(max_length=25)
    quantity = models.CharField(max_length=25)

    def __str__(self):
         return self.type

    class Meta:
        ordering = ['type']

class CoinComment(models.Model):
    name = models.CharField(max_length=150)
    title = models.TextField(max_length=150)
    statement = models.TextField(max_length=600)
    comment = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name="comments")
     
    def __str__(self):
        return self.title