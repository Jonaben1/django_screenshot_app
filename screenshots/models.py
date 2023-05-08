from django.db import models

# Create your models here.
class Screenshot(models.Model):
    url = models.CharField(max_length = 100 , blank = False,null = False)
    photo = models.ImageField(
        upload_to='images'
    )
