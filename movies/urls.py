from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path,include

router = DefaultRouter()
router.register('movies', views.MoviesViewSet)
router.register('series', views.SeriesViewSet)
router.register('season', views.SeasonViewSet)
router.register('episode', views.EpisodeViewSet)
router.register('movie_genre_item', views.MovieGenreItemViewSet)
router.register('series_genre_item', views.SeriesGenreItemViewSet)
router.register('cast', views.CastViewSet)
# router.register('actor', views.ActorViewSet)
router.register('people', views.PeopleViewSet)
router.register('genre', views.MovieGenreItemRelatedViewSet)
urlpatterns =router.urls
