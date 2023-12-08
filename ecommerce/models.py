from django.db import models
from accounts.models import Profile


# Create your models here.
class Product(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    stock = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.title}'
    
    def decrease_stock(self ,by=1):
        if self.stock < by :
            return 
        self.stock -= by