from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('movies', views.MoviesViewSet)
router.register('series', views.SeriesViewSet)
router.register('season', views.SeasonViewSet)
router.register('episode', views.EpisodeViewSet)
router.register('movie_genre_item', views.MovieGenreItemViewSet)
router.register('series_genre_item', views.SeriesGenreItemViewSet)


print(router.urls)
urlpatterns = router.urls
