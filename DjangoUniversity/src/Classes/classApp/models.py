# these entries will be translated into db tables
# pass in 'models.Model' for EVERY created class
# use 'models.CharField/TextField/etc' when defining fields
from django.db import models

# Create your models here.
class DjangoClasses(models.Model):
    Title = models.CharField(max_length=120, blank=False, null=False)
    Course_Number = models.IntegerField()
    Instructor_Name = models.CharField(max_length=60, blank=False, null=False)
    Duration = models.FloatField()

    objects = models.Manager() # sets the object's name ('Title', in this case):

    def __str__(self): # sets the object's Title:
        return self.Title
