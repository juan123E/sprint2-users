from django.urls import path, include
from usuarios.views import HomeView

urlpatterns = [
    path('',HomeView.as_view(),name='crearUsuario')
]
