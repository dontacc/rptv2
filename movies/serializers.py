from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from .models import Movie, Series, Seasons, MoviesGenresItem, SeriesGenresItem, MoviesGenres, Episodes, SeriesGenres


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


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
    class Meta:
        model = Episodes
        fields = ['id', 'title', 'create_at', ]


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
