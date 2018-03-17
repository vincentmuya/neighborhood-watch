from django import forms
from django.forms import ModelForm, Textarea
from .models import Profile,User,Post,Neighborhood


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','profile_image')

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']
        widges = {

        }

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ('neighborhood_name', 'neighborhood_location')
