from .serializers import MovieSerializer, SeriesSerializer, EpisodesSerializer, MovieGenreItemSerializer, \
    SeasonSerializer,SeriesGenreItemSerializer
from .models import Movie, Series, Seasons, MoviesGenresItem,SeriesGenresItem, MoviesGenres, Episodes,SeriesGenres
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet


class MoviesViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class SeriesViewSet(ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class SeasonViewSet(ModelViewSet):
    queryset = Seasons.objects.all()
    serializer_class = SeasonSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class EpisodeViewSet(ModelViewSet):
    queryset = Episodes.objects.all()
    serializer_class = EpisodesSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class MovieGenreItemViewSet(ReadOnlyModelViewSet):
    queryset = MoviesGenresItem.objects.all()
    serializer_class = MovieGenreItemSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class SeriesGenreItemViewSet(ReadOnlyModelViewSet):
    queryset = SeriesGenresItem.objects.all()
    serializer_class = SeriesGenreItemSerializer

    def get_serializer_context(self):
        return {'request': self.request}

