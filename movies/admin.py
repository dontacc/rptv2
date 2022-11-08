from django.contrib import admin
from .models import *


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    pass


@admin.register(MoviesGenres)
class MoviesGenresAdmin(admin.ModelAdmin):
    pass


@admin.register(SeriesGenres)
class SeriesGenresAdmin(admin.ModelAdmin):
    pass


@admin.register(Seasons)
class SeasonAdmin(admin.ModelAdmin):
    pass


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    pass


class PeopleInLine(admin.TabularInline):
    model = People
    extra = 0


@admin.register(Movie)
class CrewsAdmin(admin.ModelAdmin):
    inlines = [PeopleInLine]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Episodes)
class EpisodesAdmin(admin.ModelAdmin):
    inlines = [PeopleInLine]
