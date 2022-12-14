# Generated by Django 3.2.16 on 2022-11-12 14:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default=None, max_length=1)),
                ('image', models.ImageField(upload_to='cast/profile')),
            ],
            options={
                'verbose_name': 'cast',
                'verbose_name_plural': 'casts',
            },
        ),
        migrations.CreateModel(
            name='Episodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'episode',
                'verbose_name_plural': 'episodes',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='film/movies')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('release_date', models.CharField(max_length=255)),
                ('rate', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
            options={
                'verbose_name': 'movie',
                'verbose_name_plural': 'movies',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='film/series')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('start_at', models.CharField(max_length=255)),
                ('end_at', models.CharField(max_length=255)),
                ('rate', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
            options={
                'verbose_name': 'serie',
                'verbose_name_plural': 'series',
            },
        ),
        migrations.CreateModel(
            name='SeriesGenresItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('movies', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.series')),
            ],
            options={
                'verbose_name': 'series genre item',
                'verbose_name_plural': 'series genres items',
            },
        ),
        migrations.CreateModel(
            name='SeriesGenres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_item', models.ManyToManyField(to='movies.SeriesGenresItem')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies.series')),
            ],
            options={
                'verbose_name': 'series genre ',
                'verbose_name_plural': 'series genres ',
            },
        ),
        migrations.AddField(
            model_name='series',
            name='genre',
            field=models.ManyToManyField(to='movies.SeriesGenresItem'),
        ),
        migrations.CreateModel(
            name='Seasons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_number', models.CharField(max_length=255)),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies.series')),
            ],
            options={
                'verbose_name': 'season',
                'verbose_name_plural': 'seasons',
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=255)),
                ('cast', models.ManyToManyField(to='movies.Cast')),
                ('episodes', models.ManyToManyField(blank=True, related_name='episode', to='movies.Episodes')),
                ('films', models.ManyToManyField(blank=True, related_name='films', to='movies.Movie')),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='movies.movie')),
                ('series', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='series', to='movies.episodes')),
            ],
            options={
                'verbose_name': 'crew',
                'verbose_name_plural': 'crews',
            },
        ),
        migrations.CreateModel(
            name='MoviesGenresItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('movies', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.movie')),
            ],
            options={
                'verbose_name': 'movie genre item',
                'verbose_name_plural': 'movies genres items',
            },
        ),
        migrations.CreateModel(
            name='MoviesGenres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_item', models.ManyToManyField(to='movies.MoviesGenresItem')),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies.movie')),
            ],
            options={
                'verbose_name': 'movie genre ',
                'verbose_name_plural': 'movies genres ',
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='movies.MoviesGenresItem'),
        ),
        migrations.AddField(
            model_name='episodes',
            name='season',
            field=models.ManyToManyField(to='movies.Seasons'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
    ]
