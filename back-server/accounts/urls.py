from django.contrib import admin
from django.urls import path, include

from accounts import views

urlpatterns = [
    path('getLikeMovie/', views.getLikeMovie),

]