from django.contrib import admin
from .models import Sobre, Curso, Interesse

@admin.register(Sobre)
class SobreAdmin(admin.ModelAdmin):
    list_display = ('id', 'biografia', 'foto_perfil')
    fields = ('biografia', 'foto_perfil')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_conclusao')
    search_fields = ('nome',)
    list_filter = ('data_conclusao',)

@admin.register(Interesse)
class InteresseAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)
