from django.db import models
from django.db.models import Model, DecimalField, SmallIntegerField
from django.db.models import CharField


class Category(Model):
    name = CharField(max_length=255)

class Product(Model):
    name = CharField(max_length=255)
    price = DecimalField(max_digits=9 , decimal_places=2)
    quantity = SmallIntegerField()
