from django.db import models

# # Create your models here.
class Probnic(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)    
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['time_create'])
        ]
    
class Coach_new(models.Model):
    name = models.CharField(max_length=255)
    type_sport = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    photo = models.ImageField(upload_to='coaches/')
    is_published = models.BooleanField(default=True)

    