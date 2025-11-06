from django.urls import path
from .views import perfil, registro, editar_perfil

urlpatterns = [
    path('signup/', registro, name='registro'),
    path('profile/', perfil, name='perfil'),
    path('profile/edit/', editar_perfil, name='editar_perfil'),

]

