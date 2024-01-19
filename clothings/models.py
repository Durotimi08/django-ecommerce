from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.FloatField()
    stock=models.IntegerField(default=0, null=True)
    moq= models.IntegerField(default=0)
    image = models.ImageField(default='default.jpg', upload_to="products_pics")
    discount_percent = models.IntegerField(default=0)


    def __str__(self) :
        return self.name
    
    @property
    def discount(self):
        return self.price - (self.price * (self.discount_percent/100))
    
    
