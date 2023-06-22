from django.core.management import call_command
from django.core.management.base import BaseCommand

# To run this file "load-fixtures.py": python .\manage.py load-fixtures 
# This file should be placed in app/management/commands
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        ## call_command("makemigrations")
        ## call_command("migrate")
        ## call_command("loaddata", "auth_user.json")
        # call_command("loaddata", "1user.json")
        # call_command("loaddata", "2bancos.json")
        # call_command("loaddata", "3catorcenas.json")
        # call_command("loaddata", "4civil.json")
        # call_command("loaddata", "5contrato.json")
        # call_command("loaddata", "6datosisr.json")
        # call_command("loaddata", "7diasvacacion.json")
        # call_command("loaddata", "8distrito.json")
        # call_command("loaddata", "9empresa.json")
        # call_command("loaddata", "10factorint.json")
        # call_command("loaddata", "11nivel.json")
        # call_command("loaddata", "12proyecto.json")
        call_command("loaddata", "13puesto.json")
        call_command("loaddata", "14registropat.json")
        call_command("loaddata", "15ropa.json")
        call_command("loaddata", "16salariodatos.json")
        call_command("loaddata", "17sangre.json")
        call_command("loaddata", "18sexo.json")
        call_command("loaddata", "19subproyecto.json")
        call_command("loaddata", "20tablacesantia.json")
        call_command("loaddata", "21tablafestivos.json")
        call_command("loaddata", "22tallas.json")
        call_command("loaddata", "23tipoperfil.json")
        call_command("loaddata", "24userdatos.json")
        