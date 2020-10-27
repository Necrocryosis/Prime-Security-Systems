from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home, name="home-page"),
    path('otp/',views.generated,name="generated"),
    path('otp/home/',views.Home,name="home-page")
]