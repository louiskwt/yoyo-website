from django.shortcuts import render
from .models import Contact, HomePage, CourseInfo
from django.http import Http404

# Create your views here.
def homePageView(request):
    try: 
        heroContent = HomePage.objects.filter(section_name="heros").values_list('text_content', flat=True)

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
        raise Http404
    else:
        return render(request, 'pages/home.html', context)

    