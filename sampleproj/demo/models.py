from django.db import models

print('hello')

# Create your models here.


class Student(models.Model):
    fname = models.CharField('stud_firstname',max_length=100)
    lname = models.CharField('stud_lastname', max_length=100)
    age = models.IntegerField("stud_age")
    fees = models.FloatField("stud_fees")
    address = models.CharField('stud_address', max_length=100)
    gender = models.CharField('stud_gender', max_length=100)

    class Meta: # meta class holds-- metadata about-- student structure--metadata--additional info--> data about data
        db_table = "Stud_Info"




