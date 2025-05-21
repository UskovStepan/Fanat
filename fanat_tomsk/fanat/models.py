from django.db import models

# Create your models here.
class Coach(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='coaches/')  # фото будет сохраняться в MEDIA_ROOT/coaches/
    bio = models.TextField()
    
    def __str__(self):
        return self.name
    

class Probnic(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title