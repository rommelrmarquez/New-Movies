from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from new_movies.models import Movie

# Create your views here.

def view_upcoming_movies(request):
    '''
    '''

    context_dict = dict()
    context= RequestContext(request)
    upcoming_movies = Movie.objects.all()
    context_dict = {'upcoming_movies': upcoming_movies}

    return render_to_response('new_movies/movies.html', context_dict, context)
