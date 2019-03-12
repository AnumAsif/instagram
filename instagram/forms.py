from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Image, Comments

class SignUpForm(UserCreationForm):
    # email = forms.EmailField(max_length=254)
    full_name = forms.CharField(max_length=30, required=False)
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'use_required_attribute':False}))
    class Meta:
        model=User
        fields=('email','full_name','username','password1')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ImageForm(forms.ModelForm):  
       
    class Meta:
        model = Image
        exclude = ['likes', 'post_date', 'profile']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['image', 'user']        
    class Meta:
        model = Image
        exclude = ['likes', 'post_date', 'profile']

class CommentForm(forms.ModelForm):
    comment= forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Add a comment...'}))
    class Meta:
        model = Comments
        exclude = ['image', 'user']        