from django.contrib import admin
from django.db.models import Count

from .models import Movie,Seasons,Episodes,MoviesGenres,SeriesGenres


@admin.register(SeriesGenres)
class ChapterAdmin(admin.ModelAdmin):
    pass
@admin.register(MoviesGenres)
class ChapterAdmin(admin.ModelAdmin):
    pass
@admin.register(Seasons)
class SeasonAdmin(admin.ModelAdmin):
    # list_display = ['season']
    pass
# class ChapterInLine(admin.TabularInline):
#     model = Season
#     extra = 0
@admin.register(Episodes)
class MovieAdmin(admin.ModelAdmin):
    pass
    # list_display = ['title','description','seasons_count']
    # list_per_page = 10
    # inlines = [ChapterInLine]
    # def seasons_count(self,movie):
    #     return movie.season_set



