
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    url(r'^home/$', views.home, name = 'home'),
    url(r'^$',views.signup, name='signup'),
    url(r'profile/$', views.profile, name='profile'),
    url(r'post/$', views.addpost, name='add_post'),
    url(r'^likes/(\d+)/$', views.like, name='like')
]
if settings.DEBUG:
   urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

