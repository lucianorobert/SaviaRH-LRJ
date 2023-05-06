#from genericpath import exists
#from itertools import count
from proyecto.models import UserDatos, Perfil, Status
#from requisiciones.models import Requis
#from user.models import Profile
#Variables globales de usuario
def contadores_processor(request):
    usuario = UserDatos.objects.filter(user=request.user.id)
    #Filtro para evitar problemas al acceder los administradores sin perfil y status
    #Hace una busqueda en la database y si no lo encuentra lo guarda como ninguno y si lo encuentra lo
    #               manda a llamar en forma de get para que sea unico y no mande error
    if not UserDatos.objects.filter(user=request.user.id):
        usuario = None
        usuario_fijo = None
        status_fijo = None
    else:
        usuario = UserDatos.objects.get(user=request.user.id)
        usuario_fijo = Perfil.objects.filter(numero_de_trabajador=usuario.numero_de_trabajador, distrito=usuario.distrito)
        if not usuario_fijo:
            usuario_fijo = None
        else:
            usuario_fijo = Perfil.objects.get(numero_de_trabajador=usuario.numero_de_trabajador, distrito=usuario.distrito)
        status_fijo = Status.objects.filter(perfil__numero_de_trabajador = usuario.numero_de_trabajador, perfil__distrito = usuario.distrito)
        if not status_fijo:
            status_fijo = None
        else:
            status_fijo = Status.objects.get(perfil__numero_de_trabajador = usuario.numero_de_trabajador, perfil__distrito = usuario.distrito)
    return {
    'usuario':usuario,
    'usuario_fijo':usuario_fijo,
    'status_fijo':status_fijo,
    }