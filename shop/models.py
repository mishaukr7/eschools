from django.db import models

# Create your models here.


class News(models.Model):
    title = models.TextField(max_length=400)
    content = models.TextField(max_length=4096)
    image = models.ImageField(upload_to='shop/news/', null=True, blank=True)
    video = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created', '-updated']

