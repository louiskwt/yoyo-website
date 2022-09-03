from django.urls import path
from .views import homePageView
from django.conf.urls import handler404, handler500

app_name = "pages"

urlpatterns = [
    path("", homePageView, name="home"),
]
