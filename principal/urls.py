from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('trabajos/', views.trabajos, name="trabajos")
]
