from django.db import models

# Create your models here.
class Coach(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='coaches/')  # фото будет сохраняться в MEDIA_ROOT/coaches/
    bio = models.TextField()
    
    def __str__(self):
        return self.name