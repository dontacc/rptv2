from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from .models import Movie, Series, Seasons, Cast, MoviesGenresItem, SeriesGenresItem, MoviesGenres, Episodes, \
    SeriesGenres,People


class PeopleSerializer(serializers.ModelSerializer):

    cast=serializers.HyperlinkedRelatedField(
        many=True,
        view_name='cast-detail',
        read_only=True,
    )
    class Meta:
        model = People
        fields = [ 'job','cast']
class PeoplesmovieSerializer(serializers.ModelSerializer):

    films=serializers.HyperlinkedRelatedField(
        many=True,
        view_name='movie-detail',
        read_only=True,
    )
    episode=serializers.HyperlinkedRelatedField(
        many=True,
        view_name='movie-detail',
        read_only=True,
    )
    class Meta:
        model = People
        fields = [ 'films','episode']
class CastSerializer(serializers.ModelSerializer):

    people_set=PeoplesmovieSerializer(many=True)
    class Meta:
        model = Cast
        fields = ['id','first_name','last_name','about','age','gender','people_set']



class MovieSerializer(serializers.ModelSerializer):
    people_set = PeopleSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['title','description','release_date','people_set']


class SeriesSerializer(serializers.ModelSerializer):
    seasons_set = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='seasons-detail'
    )

    class Meta:
        model = Series
        fields = ['id', 'title', 'description', 'start_at', 'end_at', 'seasons_set']


class SeasonSerializer(serializers.ModelSerializer):
    series = StringRelatedField()
    episodes_set = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='episodes-detail')

    class Meta:
        model = Seasons
        fields = ['id', 'season_number', 'series', 'episodes_set']





class EpisodesSerializer(serializers.ModelSerializer):
    people_set = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='people-detail')
    class Meta:
        model = Episodes
        fields = ['id', 'title', 'create_at','people_set']


class MovieGenreRealationSerializer(serializers.ModelSerializer):
    movies = serializers.HyperlinkedRelatedField(
        queryset=Movie.objects.all(),
        view_name='movie-detail'

    )

    class Meta:
        model = MoviesGenres
        fields = ['movies']


class MovieGenreItemSerializer(serializers.ModelSerializer):
    moviesgenres_set = MovieGenreRealationSerializer(many=True)

    class Meta:
        model = MoviesGenresItem
        fields = ['title', 'moviesgenres_set']


class seriesGenreRealationSerializer(serializers.ModelSerializer):
    series = serializers.HyperlinkedRelatedField(
        queryset=Series.objects.all(),
        view_name='series-detail'

    )

    class Meta:
        model = SeriesGenres
        fields = ['series']


class SeriesGenreItemSerializer(serializers.ModelSerializer):
    seriesgenres_set = seriesGenreRealationSerializer(many=True)

    class Meta:
        model = SeriesGenresItem
        fields = ['title', 'seriesgenres_set']
