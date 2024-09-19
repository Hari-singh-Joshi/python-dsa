from django.db import models
from tinymce.models import HTMLField

class app1(models.Model):
    title = models.CharField(max_length=100)  # For text
    thumbnail = models.FileField(upload_to='thumbnails/', max_length=250, null=True, default=None )  # For file or PDF
    image = models.ImageField(upload_to='images/', max_length=250, null=True, default=None)  # For images
    content = models.TextField(max_length=1000,null=True,default=None)  # For large text
