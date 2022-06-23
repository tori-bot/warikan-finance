from django import forms
from .models import Profile,Account

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ( 'profile_picture','bio','gender','country','date_of_birth')

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account 
        fields = ('name','category','amount','description')
