from django.db import models

# Create your models here.


class News(models.Model):
    title = models.TextField(max_length=400)
    content = models.TextField(max_length=4096)
    video = models.URLField(blank=True, null=True)


