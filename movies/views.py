from .serializers import MovieSerializer, SeriesSerializer, EpisodesSerializer, MovieGenreItemSerializer, \
    SeasonSerializer, SeriesGenreItemSerializer,CastSerializer,PeopleSerializer,MovieGenreItemRelatedSerializer
from .models import Movie, Series, Seasons, MoviesGenresItem,SeriesGenresItem, Cast, Episodes, SeriesGenres,People
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .permission import IsAuthenticatedOrReadOnly
class MoviesViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_serializer_context(self):
        return {'request': self.request}


class SeriesViewSet(ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
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



class CastViewSet(ModelViewSet):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer

    def get_serializer_context(self):
        return {'request': self.request}

class PeopleViewSet(ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    def get_serializer_context(self):
        return {'request': self.request}

class MovieGenreItemRelatedViewSet(ModelViewSet):
    queryset = MoviesGenresItem.objects.all()
    serializer_class = MovieGenreItemRelatedSerializer

    def get_serializer_context(self):
        return {'request': self.request}