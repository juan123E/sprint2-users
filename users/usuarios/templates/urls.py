from django.urls import path, include
from usuarios.views import HomeView, EstudiantesView, ConsultasView

urlpatterns = [
    path('usuarios',HomeView.as_view(),name='crearUsuario'),
    path('estudiantes', EstudiantesView.as_view(), name='crearEstudiante'),
    path('consultas', ConsultasView.as_view(), name='consultas')
]
