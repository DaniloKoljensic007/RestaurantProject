from django.db import models

# Create your models here.


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=150, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.CharField(max_length=2083)


