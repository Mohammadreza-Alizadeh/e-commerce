from django.db import models
from accounts.models import Profile
from django.core.validators import MinValueValidator
from django.utils.safestring import mark_safe

class Product(models.Model):

    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    stock = models.IntegerField(default=0, validators=[MinValueValidator(0, 'must be greater than zero')])
    price = models.DecimalField(validators=[MinValueValidator(0)] , max_digits=10, decimal_places=2) 
    image = models.ImageField(upload_to='products', default='products/default-product.jpeg')

    def __str__(self):
        return f'{self.title}'
    

    def image_tag(self):
        return mark_safe(f'<img src="{self.image.url}" width="150" height="150" />')


    def decrease_stock(self ,by=1):
        if self.stock < by :
            return None
        self.stock -= by        
        return self.stock


class Order(models.Model):
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='orders', null=True)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1, 'must be greater than one')])
    created_date = models.DateField(auto_now_add=True)



