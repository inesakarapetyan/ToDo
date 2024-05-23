from django.db import models

# Create your models here.

class Todo(models.Model):

    todo = models.CharField('Todo name', max_length=150)
