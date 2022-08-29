from django.shortcuts import render
from .models import HomePage, CourseInfo

# Create your views here.
def homePageView(request):
    heroContent = HomePage.objects.filter(section_name="hero").values_list('text_content', flat=True)
    heroLink = HomePage.objects.filter(section_name="hero").values_list('links', flat=True)
    courseInfo = CourseInfo.objects.all()
    print(heroContent)
    context = {
        'hero': heroContent[0],
        'link': heroLink[0],
        'courseInfoList': courseInfo
    }
    return render(request, 'pages/home.html', context)