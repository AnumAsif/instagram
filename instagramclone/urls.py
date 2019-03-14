from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('instagram.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^accounts/',include('registration.backends.simple.urls')),
    url(r'^logout/$', auth_views.logout, {"next_page":'/accounts/login'}, name="logout"),
    
]
