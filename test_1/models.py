from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_pub = models.DateField(auto_now_add=True)
    date_mod = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=True)
