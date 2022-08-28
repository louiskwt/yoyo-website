from django.shortcuts import render
from django.http import HttpResponse
from .models import HomePage

# Create your views here.
def homePageView(request):
    heroContent = HomePage.objects.filter(section_name="hero").values_list('text_content', flat=True)
   
    context = {
        'hero': heroContent[0]
    }
    return render(request, 'pages/home.html', context)