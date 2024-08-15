from django.test import TestCase
from .models import Products, Order
from store.models import Customer
from store.models import Category

class ProductsModelTest(TestCase):
    def setUp(self):
        Products.objects.create(name="Test Product", price=100, description="A test product", category_id=1)

    def test_product_creation(self):
        product = Products.objects.get(name="Test Product")
        self.assertEqual(product.price, 100)
        self.assertEqual(product.description, "A test product")

class CustomerModelTest(TestCase):
    def setUp(self):
        Customer.objects.create(first_name="John", last_name="Doe", email="john@example.com", phone="1234567890", password="password")

    def test_customer_creation(self):
        customer = Customer.objects.get(email="john@example.com")
        self.assertEqual(customer.first_name, "John")
        self.assertEqual(customer.last_name, "Doe")