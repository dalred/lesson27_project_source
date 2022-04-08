from django.db import models


class Ads(models.Model):
    STATUS = [
        ("TRUE", "В наличии"),
        ("FALSE", "Недоступна"),
    ]
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.CharField(max_length=500)
    address = models.CharField(max_length=255)
    is_published = models.CharField(max_length=13, default="here", choices=STATUS)
