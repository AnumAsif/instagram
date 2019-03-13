from django.contrib import admin
from .models import Profile, Image, Comments, UserFollower, UserFollowing
# Register your models here.
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Comments)
admin.site.register(UserFollower)
admin.site.register(UserFollowing)
