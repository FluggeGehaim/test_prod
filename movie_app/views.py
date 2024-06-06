from django.shortcuts import render,get_object_or_404
from .models import Movie
from django.db.models import F, Min, Max, Avg, Count, Sum


# Create your views here.
def show_all_movies(request):
    movies = Movie.objects.order_by(F('name').asc(nulls_last=True), '-rating')
    agr = movies.aggregate(Avg('budget'), Min('rating'), Max('rating'))
    return render(request, 'movie_app/all_movies.html',
                  {'movies': movies,
                   'agr': agr,
                   'total_cnt':movies.count()})


def show_one_movie(request,slug_name:str):
    movie = get_object_or_404(Movie,slug=slug_name)
    return render(request, 'movie_app/one_movie.html',
                  {'movie':movie})
