from django.contrib import admin
from django.urls import re_path 
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path(r'^$', views.index, name='home'),
]
