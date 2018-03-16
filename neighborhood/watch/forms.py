from django import forms
from django.forms import ModelForm, Textarea
from .models import Profile,User,Post


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'neighborhood_name', 'location','profile_image')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','post')
