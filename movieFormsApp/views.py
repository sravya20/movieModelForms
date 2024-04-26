from django.shortcuts import render

from movieFormsApp.forms import MovieForm
from movieFormsApp.models import Movie


# Create your views here.
def index(request):
    return render(request, "movieModelTemplates/index.html")


def listMovies(request):
    movies = Movie.objects.all()
    return render(request, "movieModelTemplates/list_movies.html", {"movies": movies})


def addMovie(request):
    form = MovieForm()
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request, "movieModelTemplates/add_movie.html", {"movie_form": form})
