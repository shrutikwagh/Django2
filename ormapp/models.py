from calendar import month
from unicodedata import name
from django.db import models

class Emp(models.Model):
    name=models.CharField(max_length=30,null=True)
    email=models.EmailField(max_length=30,null=True)
    contact=models.CharField(max_length=15,null=True)
    age=models.IntegerField(default=0)
    address=models.TextField(max_length=300,null=True)

    def __str__(self):
        return self.name


    
class Student(models.Model):
    name=models.CharField(max_length=30,null=True)
    email=models.EmailField(max_length=30,primary_key=True)
    contact=models.CharField(max_length=15,null=True)
    age=models.IntegerField(default=0)
    address=models.TextField(max_length=300,null=True)

class singer(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    class Meta:
        db_table='singer'
        
class song(models.Model):
    name=models.CharField(max_length=30)
    duration=models.IntegerField()
    singer_n=models.ManyToManyField(singer)
    class Meta:
        db_table='song'
        
