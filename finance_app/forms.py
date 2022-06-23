from django import forms
from .models import Profile,Account

class ProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
    widget=forms.TextInput(     
        attrs={'type': 'date'} 
    )
)
    class Meta:
        model = Profile
        fields = ( 'profile_picture','bio','gender','date_of_birth','country','city')

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account 
        fields = ('name','category','amount','description')
