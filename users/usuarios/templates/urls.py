from django.urls import path, include
from usuarios.views import HomeView

urlpatterns = [
    path('crearUsuario',HomeView.as_view(),name='crearUsuario')
]
