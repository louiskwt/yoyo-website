from django.db import models

# Create your models here.
class HomePage(models.Model):
    section_name = models.CharField(max_length=50)
    links = models.TextField(null=True, blank=True)
    text_content = models.TextField()

    def __str__(self) -> str:
        return self.section_name

class CourseInfo(models.Model):
    title = models.CharField(max_length=100)
    info = models.TextField()

    def __str__(self):
        return self.title