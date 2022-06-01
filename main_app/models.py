from django.db import models

# Create your models here.
class Coin(models.Model):
    type = models.TextField(max_length=125)
    year = models.CharField(max_length=20)
    value = models.CharField(max_length=25)
    quantity = models.CharField(max_length=25)

    def __str__(self):
         return self.type

    class Meta:
        ordering = ['type']
