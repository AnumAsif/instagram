from django.contrib.auth.models import User
from django.db import models
from pyuploadcare.dj.models import ImageField
from tinymce.models import HTMLField


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_photo=ImageField(blank=True, manual_crop='800x800')
    bio=HTMLField()
  
    def __str__(self):
        return self.user.username
    
    def save_profile(self):
        self.save()

    @classmethod
    def search_profile(cls, name):
        profile=Profile.objects.filter(user__username__icontains=name)
        return profile

    @classmethod
    def get_by_id(cls, id):
        profile=Profile.objects.get(user = id)
        return profile
    
    @classmethod
    def filter_by_id(cls, id):
        profile=Profile.objects.filter(user=id).first()
        return profile

class Image(models.Model):
    image=ImageField(blank=True, manual_crop='800x800')
    image_name=models.CharField(max_length=50)
    image_caption=HTMLField(blank=True)
    post_date=models.DateTimeField(auto_now=True)
    likes=models.IntegerField(default=0)
    profile=models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-post_date',)

    def save_image(self):
        self.save()

    @classmethod
    def update_caption(cls, update):
        pass

    @classmethod
    def get_image_id(cls, id):
        image=Image.objects.get(id=id)
        return image

    @classmethod
    def get_profile_images(cls, id):
        images=Image.objects.filter(profile__pk=id)
        return images

    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images

          
class Comments(models.Model):
    comment = HTMLField()
    posted_on = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    @classmethod
    def get_comments_by_images(cls, id):
        comments = Comments.objects.filter(image__pk = id)
        return comments    

class Follow(models.Model):
    user_follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userfollower", null=True)
    user_following= models.ForeignKey(User, on_delete=models.CASCADE, related_name="userfollowing", null=True)       