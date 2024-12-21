from django.db import models
from django.db import *

# Create your models here.

# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Buyer(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=8)
    repeat_password = models.CharField(max_length=8)
    age = models.IntegerField()

    def __str__(self):
        return self.username

# python manage.py shell
# from task5.models import Buyer
# Buyer.objects.create(username='Nikita',password=123,repeat_password=123,age=14)
# Buyer.objects.create(username='Masha',password=456,repeat_password=456,age=33)
# Buyer.objects.create(username = 'Arseniy',password=456,repeat_password=465,age=52)