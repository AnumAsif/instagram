
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    url(r'^home/$', views.home, name = 'home'),
    url(r'^$',views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'post/$', views.addpost, name='add_post'),
    url(r'^likes/(\d+)/$', views.like, name='like'),
    url(r'^comments/(\d+)/$', views.comment, name='add_comment'),  
    url(r'^search/', views.search, name="search"),
    url(r'^accounts/edit/',views.edit_profile, name='edit_profile'),  
    url(r'^image/(?P<image_id>\d+)', views.image, name='image'),
]
if settings.DEBUG:
   urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

