from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, correo, nombre, apellidos, contrasena=None):
        if not correo:
            raise ValueError("El usuario debe tener un correo electrónico")
        usuario = self.model(correo=self.normalize_email(correo), nombre=nombre, apellidos=apellidos)
        usuario.set_password(contrasena)
        usuario.save(using=self._db)
        return usuario
    
    def create_superuser(self, correo, nombre, apellidos, contrasena):
        usuario = self.create_user(correo, nombre, apellidos, contrasena)
        usuario.is_admin = True
        usuario.save(using=self._db)
        return usuario

class Usuario(AbstractBaseUser):
    correo = models.EmailField(verbose_name="Correo", max_length=255, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = UsuarioManager()
    
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'apellidos']
    
    def __str__(self):
        return self.correo
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
