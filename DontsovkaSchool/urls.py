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
    re_path(r'^about$', views.about, name='about'),
    re_path(r'^students$', views.students, name='students'),
    re_path(r'^parents$', views.parents, name='parents'),
    re_path(r'^teachers$', views.teachers, name='teachers'),
    re_path(r'^educProc$', views.educProc, name='educProc'),
    re_path(r'^educProc2$', views.educProc2, name='educProc2'),
    re_path(r'^news$', views.news, name='news'),
    re_path(r'^news/(?P<newId>\d+)/', views.news, name='news'),
    re_path(r'^mail$', views.mail, name='mail'),
]
