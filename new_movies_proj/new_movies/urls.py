from django.conf.urls import patterns, url
from new_movies import views

urlpatterns = [
    url(r'^$', views.view_upcoming_movies, name='upcoming_movies'),
]
