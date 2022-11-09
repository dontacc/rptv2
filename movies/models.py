from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator
from core.models import User


class MoviesGenresItem(models.Model):
    title = models.CharField(max_length=255)
    movies = models.ForeignKey('Movie', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'movie genre item'
        verbose_name_plural = 'movies genres items'


class SeriesGenresItem(models.Model):
    title = models.CharField(max_length=255)
    movies = models.ForeignKey('Series', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'series genre item'
        verbose_name_plural = 'series genres items'


class Movie(models.Model):
    image = models.ImageField(upload_to='film/movies')
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.CharField(max_length=255)
    genre = models.ManyToManyField(MoviesGenresItem)
    rate = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'movie'
        verbose_name_plural = 'movies'


class Series(models.Model):
    image = models.ImageField(upload_to='film/series')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    start_at = models.CharField(max_length=255)
    end_at = models.CharField(max_length=255)
    genre = models.ManyToManyField(SeriesGenresItem)
    rate = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'serie'
        verbose_name_plural = 'series'


class MoviesGenres(models.Model):
    movies = models.ForeignKey(Movie, on_delete=models.PROTECT)
    genre_item = models.ManyToManyField(MoviesGenresItem)

    class Meta:
        verbose_name = 'movie genre '
        verbose_name_plural = 'movies genres '


class SeriesGenres(models.Model):
    series = models.ForeignKey(Series, on_delete=models.PROTECT)
    genre_item = models.ManyToManyField(SeriesGenresItem)

    class Meta:
        verbose_name = 'series genre '
        verbose_name_plural = 'series genres '


class Seasons(models.Model):
    season_number = models.CharField(max_length=255)
    series = models.ForeignKey(Series, on_delete=models.PROTECT)

    def __str__(self):
        return self.season_number

    class Meta:
        verbose_name = 'season'
        verbose_name_plural = 'seasons'


class Episodes(models.Model):
    title = models.CharField(max_length=255)
    season = models.ManyToManyField(Seasons)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'episode'
        verbose_name_plural = 'episodes'


class Cast(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    FEMALE = 'F'
    MALE = 'M'
    GENDER_CHOICES = [
        (FEMALE, 'Female'),
        (MALE, 'Male')
    ]
    about = models.TextField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=None)
    image = models.ImageField(upload_to='cast/profile')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'cast'
        verbose_name_plural = 'casts'


class People(models.Model):
    job = models.CharField(max_length=255)
    cast = models.ManyToManyField(Cast)
    episodes = models.ManyToManyField(Episodes, blank=True, related_name='episode')
    films = models.ManyToManyField(Movie, blank=True, related_name='films')
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, null=True, blank=True)
    series = models.ForeignKey(Episodes, on_delete=models.PROTECT, null=True, blank=True, related_name='series')

    class Meta:
        verbose_name = 'crew'
        verbose_name_plural = 'crews'


class Comment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
