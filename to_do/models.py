from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo_List(models.Model):
	title=models.CharField(max_length=200)
	description=models.CharField(max_length=500)