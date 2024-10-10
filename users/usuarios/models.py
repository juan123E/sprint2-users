from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    institucion_id = models.IntegerField()
    def __str__(self):
        return self.id

class Gestor(models.Model):
    tiposGestor = [(1,'Administrativo'), (2,'Contador'), (3,'Gestor morosos')]
    id = models.ForeignKey(Usuario, on_delete=models.CASCADE, primary_key=True)
    tipoGestor = models.CharField(max_length=50, choices=tiposGestor, null=False)
    def __str__(self):
        return self

class ResponsableFinanciero(models.Model):
    id = models.ForeignKey(Usuario, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return self.id

class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.id
    
class ResponsableEstudiante(models.Model):
    responsable_id = models.ForeignKey(ResponsableFinanciero, on_delete=models.CASCADE)  
    estudiante_id = models.ForeignKey(Estudiante, on_delete=models.CASCADE) 
    class Meta:
        unique_together = ('responsable_id', 'estudiante_id')
    def __str__(self):
        return f'Responsable: {self.responsable_id.id} - Estudiante: {self.estudiante_id.id}'
