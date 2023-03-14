from django.db import models


class Articles(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    creator = models.CharField(max_length=30, blank=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
