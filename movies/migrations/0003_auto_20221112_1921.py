# Generated by Django 3.2.16 on 2022-11-12 15:51

import ckeditor.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_auto_20221112_1848'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cast',
            options={'verbose_name': 'مشخصات بازیگر', 'verbose_name_plural': 'مشخصات بازیگران'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'نظر', 'verbose_name_plural': 'نظرها'},
        ),
        migrations.AlterModelOptions(
            name='episodes',
            options={'verbose_name': 'اپیزود', 'verbose_name_plural': 'اپیزود ها'},
        ),
        migrations.AlterModelOptions(
            name='moviesgenres',
            options={'verbose_name': 'ژانر فیلم', 'verbose_name_plural': 'ژانر فیلم ها '},
        ),
        migrations.AlterModelOptions(
            name='moviesgenresitem',
            options={'verbose_name': 'ژانر فیلم ', 'verbose_name_plural': 'ژانر فیلم ها'},
        ),
        migrations.AlterModelOptions(
            name='people',
            options={'verbose_name': 'بازیگر', 'verbose_name_plural': 'بازیگران'},
        ),
        migrations.AlterModelOptions(
            name='seasons',
            options={'verbose_name': 'فصل', 'verbose_name_plural': 'فصل ها'},
        ),
        migrations.AlterModelOptions(
            name='series',
            options={'verbose_name': 'سریال', 'verbose_name_plural': 'سریال'},
        ),
        migrations.AlterModelOptions(
            name='seriesgenres',
            options={'verbose_name': 'ژانر سریال ', 'verbose_name_plural': 'ژانر سریال ها '},
        ),
        migrations.AlterModelOptions(
            name='seriesgenresitem',
            options={'verbose_name': 'ژانر سریال ', 'verbose_name_plural': 'ژانر سریال ها'},
        ),
        migrations.RemoveField(
            model_name='episodes',
            name='title',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='seo_description',
        ),
        migrations.RemoveField(
            model_name='people',
            name='job',
        ),
        migrations.AddField(
            model_name='episodes',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='نام  اپیزود'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.CharField(default='', max_length=255, verbose_name='توضیحات'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='content',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='نام سریال'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cast',
            name='about',
            field=models.TextField(verbose_name='درباره ی'),
        ),
        migrations.AlterField(
            model_name='cast',
            name='age',
            field=models.PositiveIntegerField(verbose_name='سن'),
        ),
        migrations.AlterField(
            model_name='cast',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='cast',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default=None, max_length=1, verbose_name='ژانر'),
        ),
        migrations.AlterField(
            model_name='cast',
            name='image',
            field=models.ImageField(upload_to='cast/profile', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='cast',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='object_id',
            field=models.PositiveIntegerField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='متن نظر'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='episodes',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='episodes',
            name='season',
            field=models.ManyToManyField(to='movies.Seasons', verbose_name='فصل'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='movies.MoviesGenresItem', verbose_name='ژانر'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rate',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='امتیاز'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.CharField(max_length=255, verbose_name='تاریخ انتشار'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=255, verbose_name='موضوع'),
        ),
        migrations.AlterField(
            model_name='moviesgenres',
            name='genre_item',
            field=models.ManyToManyField(to='movies.MoviesGenresItem', verbose_name='ایتیم ژانر'),
        ),
        migrations.AlterField(
            model_name='moviesgenres',
            name='movies',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies.movie', verbose_name='فیلم'),
        ),
        migrations.AlterField(
            model_name='moviesgenresitem',
            name='movies',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.movie', verbose_name='فیلم ها'),
        ),
        migrations.AlterField(
            model_name='moviesgenresitem',
            name='title',
            field=models.CharField(max_length=255, verbose_name='ژانر'),
        ),
        migrations.AlterField(
            model_name='people',
            name='cast',
            field=models.ManyToManyField(to='movies.Cast', verbose_name='بازیگران'),
        ),
        migrations.AlterField(
            model_name='people',
            name='episodes',
            field=models.ManyToManyField(blank=True, related_name='episode', to='movies.Episodes', verbose_name='اپیزود ها'),
        ),
        migrations.AlterField(
            model_name='people',
            name='films',
            field=models.ManyToManyField(blank=True, related_name='films', to='movies.Movie', verbose_name='فیلم'),
        ),
        migrations.AlterField(
            model_name='people',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='movies.movie', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='people',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='series', to='movies.episodes', verbose_name='سریال'),
        ),
        migrations.AlterField(
            model_name='seasons',
            name='season_number',
            field=models.CharField(max_length=255, verbose_name='فصل'),
        ),
        migrations.AlterField(
            model_name='seasons',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies.series', verbose_name='سریال'),
        ),
        migrations.AlterField(
            model_name='series',
            name='description',
            field=models.CharField(max_length=255, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='series',
            name='end_at',
            field=models.CharField(max_length=255, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='series',
            name='genre',
            field=models.ManyToManyField(to='movies.SeriesGenresItem', verbose_name='ژانر'),
        ),
        migrations.AlterField(
            model_name='series',
            name='image',
            field=models.ImageField(upload_to='series/movies', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='series',
            name='rate',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='امتیاز'),
        ),
        migrations.AlterField(
            model_name='series',
            name='start_at',
            field=models.CharField(max_length=255, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='series',
            name='title',
            field=models.CharField(max_length=255, verbose_name='موضوع'),
        ),
        migrations.AlterField(
            model_name='seriesgenres',
            name='genre_item',
            field=models.ManyToManyField(to='movies.SeriesGenresItem', verbose_name='ایتیم ژانر'),
        ),
        migrations.AlterField(
            model_name='seriesgenres',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies.series', verbose_name='سریال'),
        ),
    ]
