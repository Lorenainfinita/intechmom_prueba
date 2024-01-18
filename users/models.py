# En models.py de tu aplicación Django

from django.db import models

class Users(models.Model):
    gender = models.CharField(max_length=10)
    title = models.CharField(max_length=10)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    street_number = models.IntegerField()
    street_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    email = models.EmailField()
    nationality = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class RandomUser(models.Model):
    uuid = models.CharField(max_length=50, unique=True)