from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(forms.Form):
    user_name=forms.CharField(max_length=200 , widget=forms.TextInput(attrs={'placeholder' : 'please enter user name'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' : 'please enter your email'}))
    first_name=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder' : 'please enter your name'}))
    last_name=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder' : 'please enter your family'}))
    password_1=forms.CharField(max_length=50 , widget=forms.PasswordInput(attrs={'placeholder' : 'please enter your pass'}))
    password_2=forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder' : 'please reenter your pass'}))


    def clean_user_name(self):
        user=self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('user exit')
        return user
    
    def clean_email(self):
        email=self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('email exit')
        return email
    
    def clean_password_2(self):
       password1=self.cleaned_data['password_1']
       password2=self.cleaned_data['password_2']   
       if password1 != password2 :
            raise forms.ValidationError('password not match')
       elif len(password2) < 8 :
           raise forms.ValidationError('password too short')
       elif not any (x.isupper() for x in password2):
           raise forms.ValidationError('enter a capital character for pass at least')
       return password1
    
class UserLoginForm(forms.Form):
    user = forms.CharField(max_length=200 , widget=forms.TextInput(attrs={'placeholder' : 'please enter user name'}))
    password = forms.CharField(max_length=50 , widget=forms.PasswordInput(attrs={'placeholder' : 'please enter your pass'}))





