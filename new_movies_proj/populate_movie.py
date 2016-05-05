import requests
import os
import django
from imdb_crawler import MovieCrawler

IMDB_URL = 'http://www.imdb.com/movies-coming-soon/'

def get_movies():
    '''
    '''

    crawler = MovieCrawler(IMDB_URL)
    upcoming_movies = crawler.get_upcoming_movies()
    for movie in upcoming_movies:
        # add_movie(movie)
        # retrieve cover photo
        img_file = 'new_movies/static/movies/{0}{1}'.format(movie[1], '.jpg')
        with open(img_file, 'wb') as photo:
            photo.write(requests.get(movie[0]).content)

def add_movie(movie_tuple):
    '''
    '''

    movie_inst = Movie.objects.get_or_create(title=movie_tuple[1],
                                             img_src=movie_tuple[0],
                                             rating=movie_tuple[2],
                                             description=movie_tuple[3])[0]
    return movie_inst

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new_movies_proj.settings')
    django.setup()
    from new_movies.models import Movie
    get_movies()
