from django.contrib import admin
from .models import Coach
from django.utils.safestring import mark_safe






# Register your models here.
@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo_preview')
    readonly_fields = ('photo_preview',)
    
    def photo_preview(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100" />')
        return "No photo"
    
    photo_preview.short_description = 'Preview'