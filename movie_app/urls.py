from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_all_movies),
    path('movie/<int:id_movie>',views.show_one_movie, name='look_movie')
    ]