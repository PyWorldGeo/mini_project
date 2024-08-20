from django.db import models
from django.contrib.auth.models import AbstractUser


class Type(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class User(AbstractUser):
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")



