from django.shortcuts import render
from .models import Contact, HomePage, CourseInfo


# Create your views here.
def homePageView(request):
    try: 
        heroContent = HomePage.objects.filter(section_name="hero").values_list('text_content', flat=True)

        heroLink = HomePage.objects.filter(section_name="hero").values_list('links', flat=True)

        courseInfo = CourseInfo.objects.all()

        contactList = Contact.objects.all()
        context = {
        'hero': heroContent[0],
        'link': heroLink[0],
        'courseInfoList': courseInfo,
        'contactList': contactList
        }
    except:
        return render(request, 'pages/404.html', status=404)
    else:
        return render(request, 'pages/home.html', context)
