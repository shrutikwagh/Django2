from dataclasses import fields
from django import forms
from .models import Emp,singer,song
class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields="__all__" 
        
class EmpForm2(forms.ModelForm):
    class Meta:
        model=Emp
        fields=["id","name","email","address"] 

from .models import singer,song
class singerform(forms.ModelForm):
    class Meta:
        model=singer
        fields='__all__'
        
class songform(forms.ModelForm):
    class Meta:
        model=song
        fields='__all__'

from django.contrib.auth.models import User

class userform1(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'
        
class userform2(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']