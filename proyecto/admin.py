from django.contrib import admin

from .models import Empresa
from .models import Puesto
from .models import Distrito
from .models import Proyecto
from .models import SubProyecto
from .models import Contrato
from .models import Sangre
from .models import Sexo
from .models import Civil
from .models import Banco
from .models import DatosISR
from .models import Nivel
from .models import Dia_vacacion
from .models import TablaVacaciones 
from .models import TablaFestivos
from .models import RegistroPatronal
from .models import UserDatos
from .models import TipoPerfil
from .models import Tallas
from .models import Ropa
from .models import Uniforme


from .models import Costo
from .models import Perfil
from .models import Status
from .models import DatosBancarios
from .models import Bonos
from .models import Uniformes
from .models import Vacaciones
from .models import Economicos
from .models import Catorcenas
from .models import Empleados_Batch
from .models import Status_Batch
from .models import Costos_Batch
from .models import Bancarios_Batch

class PuestoAdmin(admin.ModelAdmin):
    search_fields = ('puesto'),
    ordering = ['puesto']

class CostoAdmin(admin.ModelAdmin):
    autocomplete_fields=['puesto']

class TallaAdmin(admin.ModelAdmin):
    list_display = ('id','talla')

class DistritoAdmin(admin.ModelAdmin):
    list_display = ('id','distrito')

class PatronalAdmin(admin.ModelAdmin):
    list_display = ('id','patronal','empresa')

class SubproyectoAdmin(admin.ModelAdmin):
    list_display = ('proyecto','subproyecto')
    # Register your models here.
admin.site.register(Empresa)
admin.site.register(Puesto, PuestoAdmin)
admin.site.register(Distrito, DistritoAdmin)
admin.site.register(Proyecto)
admin.site.register(SubProyecto,SubproyectoAdmin)
admin.site.register(Contrato)
admin.site.register(Sangre)
admin.site.register(Sexo)
admin.site.register(Civil)
admin.site.register(Banco)
#Tabla niveles del empleado
admin.site.register(Nivel)
admin.site.register(Dia_vacacion)
#Tabla ISR
admin.site.register(DatosISR)
#Tabla vacaciones
admin.site.register(TablaVacaciones)
admin.site.register(TablaFestivos)
admin.site.register(RegistroPatronal, PatronalAdmin)
admin.site.register(UserDatos)
admin.site.register(TipoPerfil)
admin.site.register(Tallas, TallaAdmin)
admin.site.register(Ropa)
admin.site.register(Uniforme)

admin.site.register(Perfil)
admin.site.register(Status)
admin.site.register(Costo,CostoAdmin)
admin.site.register(DatosBancarios)
admin.site.register(Bonos)
admin.site.register(Uniformes)
admin.site.register(Vacaciones)
admin.site.register(Economicos)
admin.site.register(Catorcenas)
admin.site.register(Empleados_Batch)
admin.site.register(Status_Batch)
admin.site.register(Costos_Batch)
admin.site.register(Bancarios_Batch)