from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nuevo/', views.nuevo, name='nuevo'),
    path('ver/<int:id>', views.ver, name='ver'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('autor/<int:id>', views.autor, name='autor'),
    path('comentario/<int:id>', views.comentario, name='comentario'),
]
