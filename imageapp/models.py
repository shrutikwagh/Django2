from email.policy import default
from pyexpat import model
from django.db import models

class imagemodel(models.Model):
    name=models.CharField(max_length=30)
    img=models.ImageField(upload_to="image",default="")
    description=models.TextField(max_length=3000)
    class Meta:
        db_table="img"
from django import forms
class imageform(forms.ModelForm):
    class Meta:
        model=imagemodel
        fields='__all__'