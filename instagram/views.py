from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .forms import SignUpForm, ImageForm, CommentForm, ProfileForm
from django.contrib.auth.models import User
from .models import  Profile, Image, Comments, UserFollower,UserFollowing, ImageLike
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('registration/acc_active_email.html', {
                'user':user, 
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your instagram account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    
    else:
        form = SignUpForm()
    
    return render(request, 'registration/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required(login_url='/')
def home(request):
    user=request.user
    images=Image.objects.all()
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            image_id= request.POST['cmnt-field']
            image= Image.objects.get(id=image_id)
            comment.image=image
            comment.user=user
            comment.save()
        return redirect('home')
    else:
        form=CommentForm()
    return render(request, 'main/home.html',{'images':images, 'current_user':user, 'form':form})

@login_required(login_url='/')
def profile(request,username):
    user=User.objects.get(username=username)
    followers=UserFollower.objects.filter(user=user)
    followings=UserFollowing.objects.filter(user=user)
    posts=Image.objects.filter(profile__pk=user.id)
    current_user = request.user
    return render(request, 'main/profile.html',{'current_user':current_user,'user':user,'posts':posts, "followings":followings,"followers":followers})    

@login_required(login_url='/accounts/login')
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
    return render(request, 'main/new_post.html',{"form":form, "current_user":user})        


@login_required(login_url='/accounts/login')
def like(request,post_id):

    user=request.user
    # likes=0
    image= Image.objects.get(id=post_id)
    imagelikes= ImageLike.objects.filter(image=image, like=user)
    if not imagelikes:
        imagelike=ImageLike(image=image, like=user)
        imagelike.save()
    else:
        imagelikes.delete()    
    return redirect('home')

@login_required(login_url='/accounts/login')
def comment(request, post_id):
    
    user=request.user
    image= Image.objects.get(id=post_id)

    return redirect('home')


@login_required(login_url='/accounts/login')
def search(request):
    current_user=request.user
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        profiles = Profile.search_profile(search_term)
        message=f'{search_term}'

        return render(request, 'main/search.html', {'message':message, 'profiles':profiles, 'current_user':current_user})

    else:
        message='Enter term to search'
        return render(request, 'main/search.html',{'message':message, 'current_user':current_user})     

@login_required(login_url='/accounts/login')
def edit_profile(request):
    user=request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('edit_profile')
    else:
        form = ProfileForm()

    return render(request, 'main/edit_profile.html', {'form':form, 'current_user':user})

@login_required(login_url='/accounts/login')
def image(request, image_id):
    image = Image.get_image_id(image_id)
    comments = Comments.get_comments_by_images(image_id)
    user=request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.user = request.user
            comment.save()
            return redirect('image', image_id=image_id)
    else:
        form = CommentForm()
        
    return render(request, 'main/image.html', {'image':image, 'form':form, 'comments':comments,'current_user':user})

@login_required(login_url='/accounts/login')
def follow(request, current_user, user):
    current_user=request.user
    userfollowing=UserFollowing.objects.create(user=current_user,user_following=user)
    userfollowing.save()
    userfollower=UserFollower.objects.create(user=user, user_follower=current_user)
    userfollower.save()
    redirect('profile', username=user.username)
