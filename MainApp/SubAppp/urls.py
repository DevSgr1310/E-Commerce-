from django.contrib import admin
from django.urls import path,include
from SubAppp import views


urlpatterns = [
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact')

]