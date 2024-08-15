from django.db import models
from .category import Category

class Products(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)