from django.db import models

# Create your models here.

class School(models.Model):
    ScName = models.CharField(max_length=100,primary_key=True)
    ScPrincipal = models.CharField(max_length=100)
    ScLocation = models.CharField(max_length=100)

    def __str__(self):
        return self.ScName

class Student(models.Model):
    Sid = models.IntegerField(primary_key=True)
    Sname = models.CharField(max_length=100)
    ScName = models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return self.Sname