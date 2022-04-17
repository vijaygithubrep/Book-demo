from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=550)
    edition = models.IntegerField(max_length=100)
    author = models.CharField(max_length=250, blank=True)
    price = models.IntegerField(max_length=10)

    def __str__(self):
        return self.name

