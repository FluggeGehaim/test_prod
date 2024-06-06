from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.show_all_movies),
    path('movie/<slug:slug_name>',views.show_one_movie, name='solo_movie_path'),
]