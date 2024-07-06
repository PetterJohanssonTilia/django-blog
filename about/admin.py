from django.contrib import admin
from .models import AboutPage
from django_summernote.admin import SummernoteModelAdmin

@admin.register(AboutPage)
class AboutPageAdmin(SummernoteModelAdmin):
    list_display = ('title', 'last_updated')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)