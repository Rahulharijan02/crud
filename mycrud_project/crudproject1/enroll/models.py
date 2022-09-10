from datetime import date
from django.db import models

# Create your models here.
class User(models.Model):
    book_name = models.CharField(max_length=70)
    date = models.DateField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    number = models.CharField(max_length=100)