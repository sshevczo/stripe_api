from django.db import models
from django.urls import reverse


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=155)
    description = models.TextField(max_length=255)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def return_link(self):
        return reverse('item', args=[self.pk])
