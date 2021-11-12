from django.db import models

# Create your models here.


class Student(models.Model):
    sname = models.CharField(max_length=100)
    sid = models.IntegerField()
    sloc = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    


    def __str__(self):
        return self.sname


        