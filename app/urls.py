from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import login

urlpatterns = [
    path('', views.home,name='homepage'),
    path('about/', views.about,name='about'),
    path('post/', views.retposts,name='post'),
    path('post/<int:post_id>/', views.idposts,name='postid'),
    path('contact/', views.retcontact,name='contact'),
    path('login/', views.login,name='login'),
    #path('login/',login,{'template_name':'login.html'})
    #path('accounts/',include('django.contrib.auth.urls')),
]
