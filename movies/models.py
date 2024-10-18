from django.db import models

# Create your models here.

class Moviedata(models.Model):
    class Meta:
        verbose_name = 'Moviedata'
        verbose_name_plural = 'Moviedata'
    
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    genre = models.CharField(max_length=100, default='action')