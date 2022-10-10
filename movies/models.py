from django.db import models
from django.contrib.contenttypes.models import ContentType


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Series(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    start_at = models.CharField(max_length=255)
    end_at = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Seasons(models.Model):
    season_number = models.CharField(max_length=255)
    series = models.ForeignKey(Series, on_delete=models.PROTECT)

    def __str__(self):
        return self.season_number


class Episodes(models.Model):
    title = models.CharField(max_length=255)
    season = models.ManyToManyField(Seasons)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class MoviesGenresItem(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class SeriesGenresItem(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class MoviesGenres(models.Model):
    movies = models.ForeignKey(Movie, on_delete=models.PROTECT)
    genre_item = models.ManyToManyField(MoviesGenresItem)


class SeriesGenres(models.Model):
    series = models.ForeignKey(Series, on_delete=models.PROTECT)
    genre_item = models.ManyToManyField(SeriesGenresItem)


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    about = models.TextField()
    age = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Crews(models.Model):
    movie = models.ManyToManyField(Movie)
    season = models.ManyToManyField(Seasons)
    episode = models.ManyToManyField(Episodes)
    actor = models.ManyToManyField(Actor)
