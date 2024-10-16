from django.db import models

# Create your models here.
class Shorter(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'
