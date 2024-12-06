from django.shortcuts import render, redirect, get_object_or_404
from movies.models import Movis


def home(request):
    return render(request, 'index.html')


def movies_list(request):
    movies = Movis.objects.all()
    ctx = {'movies':movies}
    return render(request, 'movies/movies-list.html', ctx)

def movies_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        director = request.POST.get('director')
        release_year = request.POST.get('release_year')
        genre = request.POST.get('genre')
        if title and director and release_year and genre:
            Movis.objects.create(
                title=title,
                director=director,
                release_year=release_year,
                genre=genre,
            )
            return redirect('movies:list')
    return render(request, 'movies/movies-form.html')



def movies_detail(request, pk):
    movies = get_object_or_404(Movis, pk=pk)
    ctx = {'movies': movies}
    return render(request, 'movies/detail.html', ctx)


def movies_update(request, pk):
    movies = get_object_or_404(Movis, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        director = request.POST.get('director')
        release_year = request.POST.get('release_year')
        genre = request.POST.get('genre')
        if title and director and release_year and genre:
            movies.title = title
            movies.description = director
            movies.price = release_year
            movies.genre =genre
            movies.save()
            return redirect(movies.get_detail_url())
    ctx = {'movies': movies}
    return render(request, 'movies/movies-form.html', ctx)


def movies_delete(request, pk):
    movies = get_object_or_404(Movis, pk=pk)
    movies.delete()
    return redirect('movies:list')