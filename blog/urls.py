from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blogHome, name="BlogHome"),

    #Api to post a comment
    path('postComment',views.postComment,name="PostComment"),

    path('<str:slug>', views.blogPost, name="BlogPost"),

]
