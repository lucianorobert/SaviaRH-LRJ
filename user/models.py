from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save    
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from proyecto.models import UserDatos, Distrito, TipoPerfil
# Create your models here.
class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, first_name, password, **other_fields)

    def create_user(self, email, username, first_name, password, **other_fields):

        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    amaterno = models.CharField(max_length=50, null=True, blank=True)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)
    # about = models.TextField(_(
    #     'about'), max_length=500, blank=True)
    about = models.TextField(('about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    def __str__(self):
        return self.email
    
    @receiver(post_save, sender='user.User')
    def create_userDatos(sender, instance, created, **kwargs):
        if created:
            try:
                with transaction.atomic():
                    tipo_id = 2
                    tipo = TipoPerfil.objects.get(id=tipo_id)
                    distrito_id = 1  # ID of the desired distrito
                    distrito = Distrito.objects.get(id=distrito_id)
                    userDatos = UserDatos.objects.create(
                        user = instance,
                        tipo = tipo,
                        distrito = distrito,
                    )
            except ObjectDoesNotExist:
                print("Distrito does not exist")
                instance.delete()
            except Exception as e:
                print(f"Error al crear el Perfil: {e}")
                instance.delete()