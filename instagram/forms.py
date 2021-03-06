from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Image, Comments
# from tinymce.models import HTMLField

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required')
    class Meta:
        model=User
        fields=('email','username','password1','password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ImageForm(forms.ModelForm):  
    
    class Meta:
        model = Image
        exclude = ['likes', 'post_date', 'profile']
        widgets={
            'image_caption':forms.Textarea(attrs={'placeholder':'Enter your caption...'}),
            'image_name':forms.TextInput(attrs={'placeholder':'Enter Post Name...'})       }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['image', 'user']        
    
class CommentForm(forms.ModelForm):
    comment= forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Add a comment...'}))
    class Meta:
        model = Comments
        exclude = ['image', 'user']        