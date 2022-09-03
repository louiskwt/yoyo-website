from django.urls import path
from .views import homePageView

app_name = "pages"

urlpatterns = [
    path("", homePageView, name="home"),
]
