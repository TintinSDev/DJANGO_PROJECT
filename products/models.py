from django.db import models

# name,price, stock are attributes


class Product(models.Model):  # then define attributes of what is to be contained in the products
    name = models.CharField(max_length=255)  # class Character field that contains textual data
    price = models.FloatField()  # floating point numbers for prices
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)  # 2083 is the standard characters for url sites


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

