from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('sobre/', views.sobre_mim, name='sobre_mim'),
    path('cursos/', views.cursos, name='cursos'),
    path('interesses/', views.interesses, name='interesses'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
