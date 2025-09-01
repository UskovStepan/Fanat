from django.db import models
from django.urls import reverse

# Create your models here.
# class Probnic(models.Model):
#     title = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255, unique=True, db_index=True)
#     content = models.TextField(blank=True)    
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     is_published = models.BooleanField(default=True)

#     def __str__(self):
#         return self.title
    
#     class Meta:
#         ordering = ['-time_create']
#         indexes = [
#             models.Index(fields=['time_create'])
#         ]
        
    
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published = True)
    
    
class Coach_new(models.Model):
    name = models.CharField(max_length=255, verbose_name= 'ФИО тренера')
    type_sport = models.CharField(max_length=255, verbose_name= 'Вид спорта')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    photo = models.ImageField(upload_to='coaches/')
    is_published = models.BooleanField(default=True)
    
    objects = models.Manager()
    published = PublishedManager()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("show_coach", kwargs={"slug": self.slug})
    
#/__________________________________________________/   
class WeekDay(models.Model):
    name = models.CharField(max_length=15, unique=True, verbose_name= 'День недели')
    order = models.PositiveSmallIntegerField(unique=True, verbose_name= 'Порядок')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order']
        verbose_name= 'День недели'
        
        
class WorkoutType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Вид спорта')
    description = models.TextField(blank=True, verbose_name = 'Описание')
    #coach = models.ForeignKey(Coach_new, on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Вид спорта'
        
class Schedule(models.Model):
    weekday = models.ForeignKey(WeekDay, on_delete = models.PROTECT)
    workout_type = models.ForeignKey(WorkoutType, on_delete= models.PROTECT)
    trainer = models.ForeignKey(Coach_new, on_delete=models.PROTECT)
    start_time = models.TimeField(verbose_name= 'Время начала')
    end_time = models.TimeField(verbose_name= 'Время окончания')
    
    def __str__(self):
        return f'{self.weekday} {self.start_time} - {self.end_time}: {self.workout_type}'
    
    