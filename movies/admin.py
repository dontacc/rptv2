from django.contrib import admin
from .models import Movie,Seasons,Episodes,MoviesGenres,SeriesGenres,People,Series


@admin.register(SeriesGenres)
class ChapterAdmin(admin.ModelAdmin):
    pass
@admin.register(MoviesGenres)
class ChapterAdmin(admin.ModelAdmin):
    pass
@admin.register(Seasons)
class SeasonAdmin(admin.ModelAdmin):

    pass
@admin.register(People)
class SeasonAdmin(admin.ModelAdmin):

    pass
@admin.register(Episodes)
class SeasonAdmin(admin.ModelAdmin):

    pass
class PeopleInLine(admin.TabularInline):
    model = People
    extra = 0

@admin.register(Movie)
class CrewsAdmin(admin.ModelAdmin):
    inlines = [PeopleInLine]





