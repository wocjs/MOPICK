from django.urls import path
from movies import views

urlpatterns = [
    path('getmovies/', views.getMovies),
]
