from django.contrib import admin
from .models import AboutPage

# Register your models here.

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_updated')