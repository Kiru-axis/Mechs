from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from .models import Profile,Rating,Comment



class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Input a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'profile_picture', 'bio']

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['communication', 'punctuality', 'workrate']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields= ("body",)
        widgets = {
            "body":forms.Textarea(attrs={'class':'form-control'}),
        }