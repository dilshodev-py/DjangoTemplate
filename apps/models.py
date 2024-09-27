from django.db import models
from django.db.models import Model


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)  # Optional description of the category

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()
    category = models.ForeignKey('apps.Category', on_delete=models.CASCADE, related_name="products")
    description = models.TextField(blank=True, null=True)  # Optional product description
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically sets date when added
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updates on save

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey('apps.Customer', on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)  # Time when the order was created
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} for {self.customer.name}"


class OrderItem(models.Model):
    order = models.ForeignKey('apps.Order', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('apps.Product', on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.quantity} pcs"