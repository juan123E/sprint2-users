from rest_framework import serializers
from  usuarios.models import Usuario, Gestor, ResponsableFinanciero, Estudiante, ResponsableEstudiante

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
class GestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gestor
        fields = '__all__'
class ResponsableFinancieroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponsableFinanciero
        fields = ['id']
class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'
class ResponsableEstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponsableEstudiante
        fields = ['responsable_id', 'estudiante_id']

