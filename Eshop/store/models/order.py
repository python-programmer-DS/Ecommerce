from django.db import models
from .product import Products
from .customer import Customer

class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def place_order(self):
        self.save()