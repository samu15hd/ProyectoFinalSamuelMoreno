from django.urls import path
from .views import conversacion

urlpatterns = [
    path('conversacion/', conversacion, name='conversacion'),
]
