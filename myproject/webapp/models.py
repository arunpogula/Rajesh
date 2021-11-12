from django.db import models

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    sname = models.CharField(max_length=100)
    sid = models.IntegerField(unique=True)
    sloc = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete= models.CASCADE)

    def __str__(self):
        return self.sname






        