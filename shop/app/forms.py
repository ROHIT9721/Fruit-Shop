from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from .models import Contact,Fruits
    

class creatuser(UserCreationForm):
    password2=forms.CharField(label='enter again',widget=forms.PasswordInput)
    email=forms.EmailField(max_length=250,label='Email', required=True,help_text='enter a valid email')
    class Meta:
        model=User
        fields=['username','email']
class userlogin(forms.Form):
    username=forms.CharField(max_length=20, required='')
    password=forms.CharField(widget=forms.PasswordInput)


class ContactForm(forms.Form):
    Name=forms.CharField()
    Phonumber=forms.IntegerField()
    Email=forms.EmailField()
    Message=forms.CharField()
    # class Meta:
    #     model=Contact
    #     fields=['name','phonumber','email','message']


class FruitForm(forms.Form):
    Name=forms.CharField()
    about=forms.CharField()
    # im=forms.ImageField(required=False)
    # class Meta:
    #     model=Fruits
    #     fields=['id','name','about']
    #     wideget=[
    #         'name'=forms.CharField()
    #     ]


class Form(forms.Form):
    title=forms.CharField()
    about=forms.CharField()



    

    
