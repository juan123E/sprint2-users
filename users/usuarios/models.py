from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self, correo, nombre, institucion_id, password=None):
        if not correo:
            raise ValueError('El usuario debe tener un correo')
        usuario = self.model(
            correo=self.normalize_email(correo),
            nombre=nombre,
            institucion_id=institucion_id
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, correo, nombre, institucion_id, password):
        usuario = self.create_user(
            correo=self.normalize_email(correo),
            nombre=nombre,
            institucion_id=institucion_id,
            password=password
        )
        usuario.is_admin = True
        usuario.save(using=self._db)
        return usuario
class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    institucion_id = models.IntegerField()

    USERNAME_FIELD = 'correo'  # Usar correo como nombre de usuario
    PASSWORD_FIELD = 'password'  # Usar password como contraseña
    REQUIRED_FIELDS = ['nombre', 'institucion_id', 'password']  

    objects = UsuarioManager()
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
