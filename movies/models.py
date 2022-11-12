from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator
from core.models import User
from ckeditor.fields import RichTextField

class MoviesGenresItem(models.Model):
    title = models.CharField(max_length=255,verbose_name='ژانر')
    movies = models.ForeignKey('Movie', on_delete=models.SET_NULL, null=True,verbose_name='فیلم ها')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ژانر فیلم '
        verbose_name_plural = 'ژانر فیلم ها'


class SeriesGenresItem(models.Model):
    title = models.CharField(max_length=255)
    movies = models.ForeignKey('Series', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ژانر سریال '
        verbose_name_plural = 'ژانر سریال ها'


class Movie(models.Model):
    title=models.CharField(max_length=255,verbose_name='موضوع')
    description=models.CharField(max_length=255,verbose_name='توضیحات')
    image = models.ImageField(upload_to='film/movies',verbose_name='عکس')
    name = models.CharField(max_length=255,verbose_name='نام فیلم')
    content = RichTextField(blank=True,null=True,verbose_name='متن')
    release_date = models.CharField(max_length=255,verbose_name='تاریخ انتشار')
    genre = models.ManyToManyField(MoviesGenresItem,verbose_name='ژانر')
    rate = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)],verbose_name='امتیاز')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'فیلم'
        verbose_name_plural = 'فیلم ها'



class Series(models.Model):
    title = models.CharField(max_length=255, verbose_name='موضوع')
    description = models.CharField(max_length=255, verbose_name='توضیحات')
    image = models.ImageField(upload_to='series/movies', verbose_name='عکس')
    name = models.CharField(max_length=255, verbose_name='نام سریال')
    content = RichTextField(blank=True,null=True,verbose_name='متن')
    start_at = models.CharField(max_length=255,verbose_name='')
    end_at = models.CharField(max_length=255,verbose_name='')
    genre = models.ManyToManyField(SeriesGenresItem,verbose_name='ژانر')
    rate = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)],verbose_name='امتیاز')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'سریال'
        verbose_name_plural = 'سریال'


class MoviesGenres(models.Model):
    movies = models.ForeignKey(Movie, on_delete=models.PROTECT,verbose_name='فیلم')
    genre_item = models.ManyToManyField(MoviesGenresItem,verbose_name='ایتیم ژانر')

    class Meta:
        verbose_name = 'ژانر فیلم'
        verbose_name_plural = 'ژانر فیلم ها '


class SeriesGenres(models.Model):
    series = models.ForeignKey(Series, on_delete=models.PROTECT,verbose_name='سریال')
    genre_item = models.ManyToManyField(SeriesGenresItem,verbose_name='ایتیم ژانر')

    class Meta:
        verbose_name = 'ژانر سریال '
        verbose_name_plural = 'ژانر سریال ها '


class Seasons(models.Model):
    season_number = models.CharField(max_length=255,verbose_name='فصل')
    series = models.ForeignKey(Series, on_delete=models.PROTECT,verbose_name='سریال')

    def __str__(self):
        return self.season_number

    class Meta:
        verbose_name = 'فصل'
        verbose_name_plural = 'فصل ها'


class Episodes(models.Model):
    name = models.CharField(max_length=255,verbose_name='نام  اپیزود')
    season = models.ManyToManyField(Seasons,verbose_name='فصل')
    create_at = models.DateTimeField(auto_now_add=True,verbose_name='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'اپیزود'
        verbose_name_plural = 'اپیزود ها'


class Cast(models.Model):
    first_name = models.CharField(max_length=255,verbose_name='نام')
    last_name = models.CharField(max_length=255,verbose_name='نام خانوادگی')
    FEMALE = 'F'
    MALE = 'M'
    GENDER_CHOICES = [
        (FEMALE, 'Female'),
        (MALE, 'Male')
    ]
    about = models.TextField(verbose_name='درباره ی')
    age = models.PositiveIntegerField(verbose_name='سن')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=None,verbose_name='ژانر')
    image = models.ImageField(upload_to='cast/profile',verbose_name='عکس')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'مشخصات بازیگر'
        verbose_name_plural = 'مشخصات بازیگران'


class People(models.Model):
    cast = models.ManyToManyField(Cast,verbose_name='بازیگران')
    episodes = models.ManyToManyField(Episodes, blank=True, related_name='episode',verbose_name='اپیزود ها')
    films = models.ManyToManyField(Movie, blank=True, related_name='films',verbose_name='فیلم')
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, null=True, blank=True,verbose_name='')
    series = models.ForeignKey(Episodes, on_delete=models.PROTECT, null=True, blank=True, related_name='series',verbose_name='سریال')

    class Meta:
        verbose_name = 'بازیگر'
        verbose_name_plural = 'بازیگران'


class Comment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name='کاربر')
    object_id = models.PositiveIntegerField(verbose_name='')
    text = models.TextField(verbose_name='متن نظر')
    date = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ارسال')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرها'
