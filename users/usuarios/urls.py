
from django.urls import path
from usuarios.views import UsuarioViewSet, GestorViewSet, ResponsableFinancieroViewSet, EstudianteViewSet, ResponsableEstudianteViewSet

urlpatterns = [
    path('usuarios', UsuarioViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('usuarios/<str:pk>', UsuarioViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('gestores', GestorViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('gestores/<str:pk>', GestorViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('responsables', ResponsableFinancieroViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('responsables/<str:pk>', ResponsableFinancieroViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('estudiantes', EstudianteViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('estudiantes/<str:pk>', EstudianteViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('responsablesEstudiantes', ResponsableEstudianteViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('responsablesEstudiantes/<int:responsable_id>/<int:estudiante_id>', ResponsableEstudianteViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))

]
