# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Login
from .models import signup ,events_1,edit_events,delete_your_events


class loginform(forms.ModelForm):
    class Meta:
        model=Login
        fields="__all__"
        
class signupform(forms.ModelForm):
    class Meta:
        model=signup
        fields="__all__"        
        
class eventform_1(forms.ModelForm):
    class Meta:
        model=events_1
        fields="__all__"     
        
class edit_event_form(forms.ModelForm):
    class Meta:
        model=edit_events
        fields="__all__"   
                      
class delete_event_form(forms.ModelForm):
    class Meta:
        model=delete_your_events
        fields="__all__"   
                                            

