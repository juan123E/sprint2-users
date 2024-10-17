from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.response import Response
from .logic.serializers import UsuariosSerializer, GestorSerializer, ResponsableFinancieroSerializer, EstudianteSerializer, ResponsableEstudianteSerializer
from rest_framework import status
from .models import Usuario, Gestor, ResponsableFinanciero, Estudiante, ResponsableEstudiante
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

# Create your views here.
class UsuarioViewSet(viewsets.ViewSet):
    def list(self, request):#get all
        usuarios = Usuario.objects.all()
        serializer = UsuariosSerializer(usuarios, many=True)
        return Response(serializer.data)
    def create(self, request):#post
        serializer = UsuariosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def retrieve(self, request, pk=None):#get one
        usuario = Usuario.objects.get(id=pk)
        serializer = UsuariosSerializer(usuario)
        return Response(serializer.data)
    def update(self, request, pk=None):#put
        Usuario = Usuario.objects.get(id=pk)
        serializer = UsuariosSerializer(instance=Usuario, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):#delete
        usuario = Usuario.objects.get(id=pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class GestorViewSet(viewsets.ViewSet):
    def list(self, request):#get all
        gestores = Gestor.objects.all()
        serializer = GestorSerializer(gestores, many=True)
        return Response(serializer.data)
    def create(self, request):
        usuario_id = request.data.get('id')
        usuario = Usuario.objects.get(id=usuario_id)
        gestor = Gestor.objects.create(id=usuario, tipoGestor=request.data.get('tipoGestor'))
        serializer = GestorSerializer(gestor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def retrieve(self, request, pk=None):#get one
        gestor = Gestor.objects.get(id=pk)
        serializer = GestorSerializer(gestor)
        return Response(serializer.data)
    def update(self, request, pk=None):#put
        gestor = Gestor.objects.get(id=pk)
        serializer = GestorSerializer(instance=gestor, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):#delete
        gestor = Gestor.objects.get(id=pk)
        gestor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ResponsableFinancieroViewSet(viewsets.ViewSet):
    def list(self, request):#get all
        responsables = ResponsableFinanciero.objects.all()
        serializer = ResponsableFinancieroSerializer(responsables, many=True)
        return Response(serializer.data)
    def create(self, request):#post
        usuario_id = request.data.get('id')  # Obtener el ID del usuario desde el request
        
        # Validación personalizada en la vista
        if not usuario_id:
            return Response({'error': 'Se requiere el ID del usuario'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            usuario = Usuario.objects.get(id=usuario_id)  # Verificar si el usuario existe y obtener la instancia
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        # Verificar si el usuario ya tiene un responsable financiero
        if ResponsableFinanciero.objects.filter(id=usuario).exists():
            return Response({'error': 'Este usuario ya es responsable financiero'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Si pasa las validaciones, creamos el ResponsableFinanciero
        responsable = ResponsableFinanciero.objects.create(id=usuario)  # Usamos la instancia de 'usuario' aquí
        
        # Serializamos el resultado y lo retornamos
        serializer = ResponsableFinancieroSerializer(responsable)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):#get one
        responsable = ResponsableFinanciero.objects.get(id=pk)
        serializer = ResponsableFinancieroSerializer(responsable)
        return Response(serializer.data)
    def update(self, request, pk=None):#put
        responsable = ResponsableFinanciero.objects.get(id=pk)
        serializer = ResponsableFinancieroSerializer(instance=responsable, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):#delete
        responsable = ResponsableFinanciero.objects.get(id=pk)
        responsable.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EstudianteViewSet(viewsets.ViewSet):
    def list(self, request):#get all
        estudiantes = Estudiante.objects.all()
        serializer = EstudianteSerializer(estudiantes, many=True)
        return Response(serializer.data)
    def create(self, request):#post
        serializer = EstudianteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def retrieve(self, request, pk=None):#get one
        estudiante = Estudiante.objects.get(id=pk)
        serializer = EstudianteSerializer(estudiante)
        return Response(serializer.data)
    def update(self, request, pk=None):#put
        estudiante = Estudiante.objects.get(id=pk)
        serializer = EstudianteSerializer(instance=estudiante, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):#delete
        estudiante = Estudiante.objects.get(id=pk)
        estudiante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ResponsableEstudianteViewSet(viewsets.ViewSet):
    def list(self, request):#get all
        responsables = ResponsableEstudiante.objects.all()
        serializer = ResponsableEstudianteSerializer(responsables, many=True)
        return Response(serializer.data)
    def create(self, request):#post
        responsable_id = request.data.get('responsable_id')
        estudiante_id = request.data.get('estudiante_id')
        responsable = ResponsableFinanciero.objects.get(id=responsable_id)
        estudiante = Estudiante.objects.get(id=estudiante_id)
        responsableEstudiante = ResponsableEstudiante.objects.create(responsable_id=responsable, estudiante_id=estudiante)
        serializer = ResponsableEstudianteSerializer(responsableEstudiante)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def retrieve(self, request, pk=None):#get one
        responsable_estudiante = self.get_object()  # Obtiene el objeto específico
        serializer = self.get_serializer(responsable_estudiante)
        return Response(serializer.data)
    def update(self, request, pk=None):#put
        responsable = ResponsableEstudiante.objects.get(id=pk)
        serializer = ResponsableEstudianteSerializer(instance=responsable, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):#delete
        responsable = ResponsableEstudiante.objects.get(id=pk)
        responsable.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class HomeView(TemplateView):
    template_name = 'crearUsuarios.html'
    