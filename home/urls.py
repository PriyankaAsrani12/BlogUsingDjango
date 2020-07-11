from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('contact', views.contact, name="Contact"),
    path('about', views.about, name="About"),
    path('search', views.search, name="Search"),
    path('signup', views.handleSignup, name="Signup"),
    path('login', views.handleLogin, name="Login"),
    path('logout', views.handleLogout, name="Logout"),
]