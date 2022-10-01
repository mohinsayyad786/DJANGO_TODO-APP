from dataclasses import field
from django import forms
from todoapp.models import Course
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class EmpRegister(forms.Form):

    name=forms.CharField()
    email=forms.CharField()
    mobile=forms.CharField()

class CourseForm(forms.ModelForm):
    course_name=forms.CharField()
    course_duration=forms.IntegerField()
    course_category=forms.CharField()
    course_fees=forms.FloatField()


    class Meta:
        model=Course
        #fields="__all__"
        fields=["course_name",'course_duration','course_category','course_fees']
class RegisterForm(UserCreationForm):

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']