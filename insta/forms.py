from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field


class PostForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Post', 'Post', css_class='btn-primary'))

    class Meta:
        model = Post
        fields = [
            'image',
            'caption'
        ]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    bio = forms.Textarea()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']