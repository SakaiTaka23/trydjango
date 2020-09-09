from django.db import models
from django.urls import reverse

# Create your models here.


class Courses(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
