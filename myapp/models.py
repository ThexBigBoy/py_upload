from django.db import models

# Create your models here.
class StudentForm(models.Model):
    firstname = models.CharField("Enter Name", max_length=50)
    lastname = models.CharField("Enter Username", max_length=50)
    email = models.CharField("Enter Description", max_length=100)
    file = models.ImageField()
    
    class Meta:
        db_table = "student"


