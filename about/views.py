from django.shortcuts import render
from .models import AboutPage

# Create your views here.

def about_view(request):
    about_content = AboutPage.objects.first()
    return render(request, 'about/about.html', {'about_content': about_content})