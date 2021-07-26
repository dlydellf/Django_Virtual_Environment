from django.db import models

# Create your models here.
class DjangoClasses(models.Model):
    Title = models.CharField(max_length=120, blank=False, null=False)
    Course_Number = models.IntegerField()
    Instructor_Name = models.CharField(max_length=60, blank=False, null=False)
    Duration = models.FloatField()
