from abc import abstractstaticmethod
from PIL import Image
from django import forms
from django.forms import widgets
from django.forms.fields import CharField, DateField, ImageField
import datetime

class UploadImage(forms.Form):
    poster = forms.IntegerField(widget=forms.HiddenInput(attrs={}))
    image = forms.ImageField(required = True,widget=forms.FileInput(attrs={'onchange':'readURL(this);','id':'file-ip-1'}))
    date = forms.DateTimeField(widget=forms.DateTimeInput(format = '2006-10-25 14:30:59',attrs={'class':'form-control-lg col m-2','placeholder':'2006-10-25 14:30:59'}))
    location = forms.CharField(required = True, widget=forms.TextInput(attrs={'class':'form-control-lg col m-2', 'placeholder': 'Where are You?'}))
    hashtags = forms.CharField(required = True, widget=forms.TextInput(attrs={'class': 'form-control col m-2', 'placeholder': '#Hashtags','id':'hashtag'}))
    taggedpeeps = forms.CharField(required = True, widget=forms.TextInput(attrs={'class': 'form-control col m-2', 'placeholder': 'Tag People','id':'taggedpeeps'}))
    caption = forms.CharField(required = True,widget = forms.Textarea(attrs={'class':'form-control col m-4', 'placeholder': 'Caption','id':'caption'}))