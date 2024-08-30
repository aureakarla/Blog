from django.urls import path
from . import views
import include
import admin

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', views.index, name='index'),
    path('sobre/', views.sobre_mim, name='sobre_mim'),
    path('cursos/', views.cursos, name='cursos'),
    path('interesses/', views.interesses, name='interesses'),
]
