from django.db import models

# Create your models here.
class Design(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=50)
    design=models.ForeignKey(Design, on_delete= models.CASCADE)

    def __str__(self):
        return self.name

class Cart(models.Model):
    customer_name=models.CharField(max_length=50)
    products=models.ManyToManyField(Product)

    def __str__(self):
        return self.customer_name
