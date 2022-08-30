from django.contrib import admin
from .models import HomePage, CourseInfo, Contact

# Register your models here.
admin.site.register(HomePage)
admin.site.register(CourseInfo)
admin.site.register(Contact)