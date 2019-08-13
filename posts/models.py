'''
from django.db import models
from django.contrib.postgres.fields import ArrayField

from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    pic = models.ImageField()
    comments = models.TextField()
    # tags = ArrayField(models.CharField(max_length=20, blank=False, default='NO TAG'))
'''
    