from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .forms import SignUpForm, ImageForm
from django.contrib.auth.models import User
from .models import  Image, Comments, Follow
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.refresh_from_db()
            user.profile.username = form.cleaned_data.get('username')
            user.is_active=False
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def home(request):
    user=request.user
    images=Image.objects.all()
    
    return render(request, 'main/home.html',{'images':images, 'user':user})

def profile(request):
    user=request.user
    following =0
    followers=0
    # user = User.objects.filter(username='anum').first()
    posts=Image.objects.filter(profile__pk=user.id)
    
    return render(request, 'main/profile.html',{'user':user,'posts':posts, "following":following,"followers":followers})    

def addpost(request):
    user=request.user
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            image=form.save(commit=False)
            image.profile=user
            image.save()
        return redirect('home')
    else:
        form=ImageForm()
    return render(request, 'main/new_post.html',{"form":form})        

def like(request,post_id):
    user=request.user    