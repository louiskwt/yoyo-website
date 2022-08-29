from .models import HomePage

def base_context(request):
    link = HomePage.objects.filter(section_name="hero").values_list('links', flat=True)
    return {'link': link}
