from django.shortcuts import render
from django.http import HttpResponse
from .models import HomePage, CourseInfo

# Create your views here.
def homePageView(request):
    heroContent = HomePage.objects.filter(section_name="hero").values_list('text_content', flat=True)
    courseInfo = CourseInfo.objects.all()
    print(courseInfo)
    context = {
        'hero': heroContent[0],
        'courseInfoList': courseInfo
    }
    return render(request, 'pages/home.html', context)