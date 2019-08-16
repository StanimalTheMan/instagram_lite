from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError

def validate_picture(picture):
    file_size = picture.file.file_size
    limit_kb = 150
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='pics/', validators=[validate_picture])
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    