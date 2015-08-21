from django.db import models


class Menu(models.Model):
    """Model represent a menu of services"""
    name = models.CharField(max_length=80)


class Category(models.Model):
    menu = models.ForeignKey('Menu', related_name='categories')
    name = models.CharField(max_length=40)


class Product(models.Model):
    category = models.ForeignKey('Category', related_name='products')
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
