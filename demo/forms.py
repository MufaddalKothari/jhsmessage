from django import forms

class NewUser(forms.Form):
    email = forms.EmailField(max_length=23,min_length=23,required = True,widget=forms.TextInput(attrs={'placeholder': 'JHS Email'}))
    password = forms.CharField(required = True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class UpdatePassword(forms.Form):
    oldpassword = forms.CharField(required = True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    newpassword = forms.CharField(required = True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))