from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.http import FileResponse

from django.db.models import Sum
from django.contrib import messages
import locale
locale.setlocale( locale.LC_ALL, '' )

from .models import DatosISR, Costo, TablaVacaciones, Perfil, Status, Uniformes, DatosBancarios, Bonos, Vacaciones, Economicos, Puesto, Empleados_Batch, RegistroPatronal, Banco
from .models import Status_Batch, Empresa, Distrito, Nivel, Contrato, Sangre, Sexo, Civil, UserDatos, Catorcenas, Uniforme, Tallas, Ropa, SubProyecto, Proyecto,Costos_Batch, Bancarios_Batch
import csv
import json
#from django.contrib.auth.decorators import login_required
#from .filters import ArticulosparaSurtirFilter
from django.http import HttpResponse
import datetime
from datetime import timedelta, date
from django.db.models.functions import Concat
#PDF generator
from django.db.models import Q
from collections import Counter
from .forms import CostoForm, BonosForm, VacacionesForm, EconomicosForm, UniformesForm, DatosBancariosForm, PerfilForm, StatusForm, IsrForm,PerfilUpdateForm
from .forms import CostoUpdateForm, BancariosUpdateForm, BonosUpdateForm, VacacionesUpdateForm, EconomicosUpdateForm, StatusUpdateForm, CatorcenasForm
from .forms import Dias_VacacionesForm, Empleados_BatchForm, Status_BatchForm, PerfilDistritoForm, UniformeForm, Costos_BatchForm, Bancarios_BatchForm
from .filters import BonosFilter, Costo_historicFilter, PerfilFilter, StatusFilter, BancariosFilter, CostoFilter, VacacionesFilter, UniformesFilter, EconomicosFilter
from .filters import CatorcenasFilter
from decimal import Decimal
#Excel
from openpyxl import Workbook
from openpyxl.styles import NamedStyle, Font, PatternFill
from openpyxl.utils import get_column_letter
from django.db.models.functions import Concat
from django.db.models import Value
from django.forms import inlineformset_factory
from itertools import chain

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch,cm,mm
from reportlab.lib.pagesizes import letter,A4,landscape
import io
from reportlab.lib import colors
from reportlab.lib.colors import Color, black, blue, red, white
from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, NextPageTemplate, PageBreak, PageTemplate,Table, SimpleDocTemplate,TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.utils import ImageReader
import os

def Principal(request):
    return render(request, 'proyecto/Principal.html')

def Index(request):
    return render(request, 'proyecto/Inicio.html')


def Tabla_isr(request):

    isrs= DatosISR.objects.all()

    context= {
        'isrs':isrs,
        }

    return render(request, 'proyecto/Tabla_isr.html',context)

def Tabla_catorcenas(request):

    catorcenas = Catorcenas.objects.filter(complete=True)

    catorcena_filter = CatorcenasFilter(request.GET, queryset=catorcenas)
    catorcenas = catorcena_filter.qs
    context= {
        'catorcenas':catorcenas,
        'catorcena_filter':catorcena_filter,
        }

    return render(request, 'proyecto/Tabla_catorcenas.html',context)

def FormularioCatorcenas(request):
    catorcena,created=Catorcenas.objects.get_or_create(complete=False)
    form = CatorcenasForm()
    if request.method == 'POST' and 'btnSend' in request.POST:
        form = CatorcenasForm(request.POST,instance=catorcena)
        form.save(commit=False)

        if form.is_valid():
            messages.success(request, 'Catorcena capturada con éxito')
            catorcena.complete=True
            form.save()
            return redirect('Tabla_catorcenas')
    context = {'form':form,}

    return render(request, 'proyecto/CatorcenasForm.html',context)

def CatorcenasUpdate(request, pk):

    item = Catorcenas.objects.get(id=pk)

    if request.method == 'POST':
        form = CatorcenasForm(request.POST, instance=item)

        if form.is_valid():
            messages.success(request, 'Cambios guardados con éxito en la catorcena')
            item = form.save(commit=False)
            item.save()

            catorcenas = Catorcenas.objects.filter(complete=True)
            bonos = Bonos.objects.filter(complete=True)
            for bono in bonos:
                for catorcena in catorcenas:
                    if bono.fecha_bono >= catorcena.fecha_inicial:
                        bono.mes_bono = catorcena.fecha_final
                        bono.save()

            return redirect('Tabla_catorcenas')
    else:
        form = CatorcenasForm(instance=item)

    context = {'form':form,'item':item}

    return render(request, 'proyecto/Catorcenas_update.html',context)

def IsrUpdate(request, pk):

    item = DatosISR.objects.get(id=pk)

    if request.method == 'POST':
        form = IsrForm(request.POST, instance=item)

        messages.success(request, 'Cambios guardados con éxito en la tabla ISR')
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('Tabla_isr')
    else:
        form = IsrForm(instance=item)

    context = {'form':form,'item':item}

    return render(request, 'proyecto/Isr_update.html',context)

def Dias_VacacionesUpdate(request, pk):

    item = TablaVacaciones.objects.get(id=pk)

    if request.method == 'POST':
        form = Dias_VacacionesForm(request.POST, instance=item)

        messages.success(request, 'Cambios guardados con éxito en la tabla días de vacaciones')
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('Tabla_isr')
    else:
        form = Dias_VacacionesForm(instance=item)

    context = {
        'form':form,
        'item':item,
        }

    return render(request, 'proyecto/Dias_vacaciones_update.html',context)


def Tabla_dias_vacaciones(request):
    año = datetime.date.today().year
    descansos= TablaVacaciones.objects.all()

    context= {
        'descansos':descansos,
        }

    return render(request, 'proyecto/Tabla_dias_vacaciones.html',context)

def Perfil_vista(request): # Ya esta
    user_filter = UserDatos.objects.get(user=request.user)

    if user_filter.distrito.distrito == 'Matriz':
        perfiles= Perfil.objects.filter(complete=True).order_by("numero_de_trabajador")
    else:
        perfiles= Perfil.objects.filter(distrito=user_filter.distrito,complete=True).order_by("numero_de_trabajador")
    perfil_filter = PerfilFilter(request.GET, queryset=perfiles)
    perfiles = perfil_filter.qs
    if request.method =='POST' and 'Excel' in request.POST:
        return convert_excel_perfil(perfiles)

    context= {
        'perfiles':perfiles,
        'perfil_filter':perfil_filter,
        }

    return render(request, 'proyecto/Perfil.html',context)

def FormularioPerfil(request):
    user_filter = UserDatos.objects.get(user=request.user)
    empleado,created=Perfil.objects.get_or_create(complete=False)
    subproyectos = SubProyecto.objects.all()

    if user_filter.distrito.distrito == 'Matriz':
        form = PerfilForm()
    else:
        form = PerfilDistritoForm()
    ahora = datetime.date.today()

    if request.method == 'POST' and 'btnSend' in request.POST:
        form = PerfilForm(request.POST, request.FILES, instance=empleado)
        form.save(commit=False)

        if empleado.foto and empleado.foto.size > 500000:
            messages.error(request,'El tamaño del archivo es mayor de 500 MB')
        elif empleado.numero_de_trabajador <= 0:
            messages.error(request, '(Número empleado) El numero de empleado debe ser mayor a 0')
        elif empleado.fecha_nacimiento >= ahora:
            messages.error(request, 'La fecha de nacimiento no puede ser mayor o igual a hoy')
        elif Perfil.objects.filter(numero_de_trabajador=empleado.numero_de_trabajador):
            messages.error(request, '(Número empleado) El numero de empleado se repite con otro')
        else:
            messages.success(request, 'Información capturada con éxito')
            if form.is_valid():
                empleado.complete=True
                form.save()
                return redirect('Perfil')

    context = {
        'form':form,
        'subproyectos':subproyectos
        }

    return render(request, 'proyecto/PerfilForm.html',context)


def PerfilUpdate(request, pk):
    empleado = Perfil.objects.get(id=pk)
    ahora = datetime.date.today()
    subproyectos = SubProyecto.objects.all()

    if request.method == 'POST' and 'btnSend' in request.POST:
        #request.FILES permite subir imagenes en el form
        form = PerfilUpdateForm(request.POST, request.FILES, instance=empleado)
        empleado = form.save(commit=False)
        if empleado.foto and empleado.foto.size > 500000:
            messages.error(request,'El tamaño del archivo es mayor de 500 MB')
        elif empleado.fecha_nacimiento >= ahora:
            messages.error(request, 'La fecha de nacimiento no puede ser mayor o igual a hoy')
        elif form.is_valid():
            #messages.success(request, f'Cambios guardados con éxito en el perfil de {empleado.nombres} {empleado.apellidos} {empleado.foto.size}')
            messages.success(request, f'Cambios guardados con éxito en el perfil de {empleado.nombres} {empleado.apellidos}')
            empleado = form.save(commit=False)
            empleado.save()
            return redirect('Perfil')
    else:
        form = PerfilUpdateForm(instance=empleado)

    context = {
        'form':form,
        'empleado':empleado,
        'subproyectos':subproyectos,
        }


    return render(request, 'proyecto/Perfil_update.html',context)

def Perfil_revisar(request, pk):

    empleado = Perfil.objects.get(id=pk)


    context = {
        'empleado':empleado,

        }

    return render(request, 'proyecto/Perfil_revisar.html',context)


def Status_vista(request): #Ya esta
    user_filter = UserDatos.objects.get(user=request.user)

    if user_filter.distrito.distrito == 'Matriz':
        status= Status.objects.filter(complete=True).order_by("perfil__numero_de_trabajador")
    else:
        status = Status.objects.filter(perfil__distrito = user_filter.distrito, complete=True).order_by("perfil__numero_de_trabajador")

    #status= Status.objects.filter(complete=True)
    status_filter = StatusFilter(request.GET, queryset=status)
    status = status_filter.qs
    if request.method =='POST' and 'Excel' in request.POST:
        return convert_excel_status(status)
    context= {
        'status':status,
        'status_filter':status_filter,
        }

    return render(request, 'proyecto/Status.html',context)

def FormularioStatus(request):
    user_filter = UserDatos.objects.get(user=request.user)

    if user_filter.distrito.distrito == 'Matriz':
        empleados = Perfil.objects.filter(complete=True, complete_status=False)
    else:
        empleados = Perfil.objects.filter(distrito=user_filter.distrito,complete=True, complete_status=False)

    #empleados = Perfil.objects.filter(complete=True, complete_status=False)
    estado,created=Status.objects.get_or_create(complete=False)
    form = StatusForm()
    ahora = datetime.date.today()
    registro_patronal = RegistroPatronal.objects.all()

    if request.method == 'POST' and 'btnSend' in request.POST:
        form = StatusForm(request.POST,instance=estado)
        form.save(commit=False)
        if estado.fecha_planta_anterior == None:
            estado.fecha_planta_anterior = estado.fecha_planta
        if estado.fecha_planta_anterior >= ahora:
            messages.error(request, '(Fecha planta anterior) La fecha no puede ser posterior a hoy')
        else:
            if estado.fecha_planta >= ahora:
                messages.error(request, '(Fecha planta) La fecha no puede ser posterior a hoy')
            else:
                if estado.fecha_planta < estado.fecha_planta_anterior:
                    messages.error(request, '(Fechas) La fecha de planta anterior no puede ser posterior a la fecha de planta')
                else:
                    empleado = Perfil.objects.get(id = estado.perfil.id)
                    if form.is_valid():
                        messages.success(request, 'Información capturada con éxito')
                        estado.complete=True
                        form.save()
                        estado.save()
                        empleado.complete_status=True
                        empleado.save()
                        return redirect('Status')

    context = {
        'form':form,
        'empleados':empleados,
        'registro_patronal': registro_patronal,
        }

    return render(request, 'proyecto/StatusForm.html',context)

def StatusUpdate(request, pk):
    estado = Status.objects.get(id=pk)
    ahora = datetime.date.today()
    if request.method == 'POST' and 'btnSend' in request.POST:
        form = StatusUpdateForm(request.POST, instance=estado)
        estado = form.save(commit=False)
        if estado.fecha_planta_anterior >= ahora:
            messages.error(request, '(Fecha planta anterior) La fecha no puede ser posterior a hoy')
        elif estado.fecha_planta >= ahora:
            messages.error(request, '(Fecha planta) La fecha no puede ser posterior a hoy')
        elif estado.fecha_planta <= estado.fecha_planta_anterior:
            messages.error(request, '(Fechas) La fecha de planta anterior no puede ser posterior o igual a la fecha de planta')
        elif form.is_valid():
            messages.success(request, f'Cambios guardados con éxito en el Status de {estado.perfil.nombres} {estado.perfil.apellidos}')
            estado = form.save(commit=False)
            estado.save()
            return redirect('Status')
    else:
        form = StatusUpdateForm(instance=estado)

    context = {'form':form,'estado':estado}

    return render(request, 'proyecto/Status_update.html',context)

def Status_revisar(request, pk):

    estado = Status.objects.get(id=pk)


    context = {'estado':estado,}

    return render(request, 'proyecto/Status_revisar.html',context)

def Admininistrar_tablas(request):
    return render(request, 'proyecto/Administrar_tablas.html')

def FormularioBonos(request):
    user_filter = UserDatos.objects.get(user=request.user)

    if user_filter.distrito.distrito == 'Matriz':
        empleados= Costo.objects.filter(complete = True)
    else:
        perfil = Perfil.objects.filter(distrito = user_filter.distrito)
        empleados= Costo.objects.filter(status__perfil__id__in=perfil.all(),complete = True)

    bonos= Bonos.objects.filter(complete=True)
    catorcenas = Catorcenas.objects.filter(complete=True)
    bono,created=Bonos.objects.get_or_create(complete=False)
    form = BonosForm()
    #empleados = Costo.objects.filter(complete=True)
    if request.method == 'POST':
        form = BonosForm(request.POST,instance=bono)
        form.save(commit=False)

        trabajador = bono.costo.status
        user = DatosBancarios.objects.filter(status=trabajador).last()
        if user is None:
            messages.error(request, '(Empleado) El empleado no tiene datos bancarios')
        else:
            bono.datosbancarios = user
            if bono.monto < 0:
                messages.error(request, '(Monto) La cantidad capturada debe ser mayor o igual 0')
            else:
                for catorcena in catorcenas:
                    if bono.fecha_bono >= catorcena.fecha_inicial:
                        bono.mes_bono = catorcena.fecha_final
                if form.is_valid():
                    messages.success(request, 'Información capturada con éxito')
                    bono.complete=True
                    form.save()
                    return redirect('Tabla_bonos')
    context = {'form':form,'bonos':bonos,'empleados':empleados,}

    return render(request, 'proyecto/BonosForm.html',context)

def BonosUpdate(request, pk):
    bono = Bonos.objects.get(id=pk)
    catorcenas = Catorcenas.objects.filter(complete=True)
    if request.method == 'POST':
        form =BonosUpdateForm(request.POST, instance=bono)
        bono = form.save(commit=False)
        if bono.monto < 0:
            messages.error(request, '(Monto) La cantidad capturada debe ser mayor o igual 0')
        else:
            for catorcena in catorcenas:
                if bono.fecha_bono >= catorcena.fecha_inicial:
                    bono.mes_bono = catorcena.fecha_final
        if form.is_valid():
            messages.success(request, f'Cambios guardados con éxito en los bonos de {bono.costo.status.perfil.nombres} {bono.costo.status.perfil.apellidos}')
            bono = form.save(commit=False)
            bono.save()
            return redirect('Tabla_bonos')
    else:
        form = BonosUpdateForm(instance=bono)

    context = {'form':form,'bono':bono}

    return render(request, 'proyecto/Bonos_update.html',context)

def Tabla_uniformes(request):
    user_filter = UserDatos.objects.get(user=request.user)

    if user_filter.distrito.distrito == 'Matriz':
        status= Status.objects.filter(complete=True)
    else:
        perfil = Perfil.objects.filter(distrito = user_filter.distrito)
        status= Status.objects.filter(complete=True,perfil__id__in=perfil.all())

    status_filter = StatusFilter(request.GET, queryset=status)
    status = status_filter.qs
    if request.method =='POST' and 'Excel' in request.POST:
        return convert_excel_uniformes(status)

    context= {
        'status':status,
        'status_filter':status_filter,
        }

    return render(request, 'proyecto/Tabla_uniformes.html',context)

def Orden_uniformes(request, pk):
    status = Status.objects.get(id=pk)
    orden, created=Uniformes.objects.get_or_create(complete=False, status= status)
    ropas = Ropa.objects.filter(seleccionado=False)
    form = UniformesForm(instance=orden)
    form_uniforme = UniformeForm()
    uniformes_pedidos = Uniforme.objects.filter(orden=orden)

    #for item in uniformes_pedidos:
    #    total_uniformes = total_uniformes + item.cantidad

    if request.method == 'POST' and  "crear" in request.POST:
        form = UniformesForm(request.POST, instance=orden)
        if uniformes_pedidos.count() == 0:
            messages.error(request, 'Debe añadir al menos un elemento a la Orden')
        else:
            empleado = Status.objects.get(id=pk)
            if form.is_valid():
                messages.success(request, 'Orden realizada con exito')

                empleado.complete_uniformes = True
                orden.complete = True
                form.save()
                orden.save()
                empleado.save()
                return redirect('Tabla_uniformes')

    context= {
        'form':form,
        'status':status,
        'orden':orden,
        'form_uniforme':form_uniforme,
        'uniformes_pedidos':uniformes_pedidos,
        'ropas':ropas,
        }

    return render(request, 'proyecto/Uniformes_ordenes.html',context)


def update_uniformes(request, pk):
    data= json.loads(request.body)
    action = data['action']
    orden_id = int(data['orden_id'])
    ropa_id = int(data['uniforme'])
    talla_id = int(data['talla'])
    cantidad = int(data['cantidad'])
    orden = Uniformes.objects.get(id = orden_id)
    ropa = Ropa.objects.get(id = ropa_id)
    talla = Tallas.objects.get(id=talla_id)
    producto, created = Uniforme.objects.get_or_create(orden = orden, ropa = ropa, talla = talla)
    if action == "add":
        producto.cantidad = cantidad
        ropa.seleccionado = True
        producto.complete = True
        ropa.save()
        producto.save()
        messages.success(request,f'Se agregan {producto.cantidad} {producto.ropa} a la orden')
    if action == "remove":
        ropa.seleccionado = False
        ropa.save()
        producto.delete()

    return JsonResponse('Item updated, action executed: '+data["action"], safe=False)

#def Uniformes_revisar(request, pk):

#    ropa = Uniformes.objects.get(status.id=pk)
#    orden = Uniforme.objects.filter(id=pk)

#    context = {'ropa':ropa,'orden':orden}

#    return render(request, 'proyecto/Uniformes_revisar.html',context)


def Uniformes_revisar_completados(request, pk):

    ropas = Uniformes.objects.filter(status_id=pk)
    perfil = Status.objects.get(id=pk)
    #uniformes = Uniforme.objects.filter(orden__status_id=pk)

    context = {'ropas':ropas,'perfil':perfil,}

    return render(request, 'proyecto/Uniformes_revisar_completados.html',context)

def Uniformes_revisar_ordenes(request, pk):

    ordenes = Uniforme.objects.filter(orden_id=pk)
    pedido = Uniformes.objects.get(id=pk)
    #uniformes = Uniforme.objects.filter(orden__status_id=pk)

    context = {'ordenes':ordenes,'pedido':pedido,}

    return render(request, 'proyecto/Uniformes_revisar_ordenes.html',context)

def FormularioDatosBancarios(request):
    user_filter = UserDatos.objects.get(user=request.user)

    if user_filter.distrito.distrito == 'Matriz':
        empleados= Status.objects.filter(complete = True, complete_bancarios=False)
    else:
        perfil = Perfil.objects.filter(distrito = user_filter.distrito)
        empleados= Status.objects.filter(perfil__id__in=perfil.all(),complete = True, complete_bancarios=False)

    #empleados= Status.objects.filter(complete = True, complete_bancarios=False)
    bancario,created=DatosBancarios.objects.get_or_create(complete=False)
    form = DatosBancariosForm()

    if request.method == 'POST' and 'btnSend' in request.POST:
        form = DatosBancariosForm(request.POST,instance=bancario)
        form.save(commit=False)

        if form.is_valid():
            empleado = Status.objects.get(id = bancario.status.id)
            messages.success(request, 'Información capturada con éxito')
            bancario.complete=True
            empleado.complete_bancarios = True
            form.save()
            empleado.save()
            return redirect('Tabla_datosbancarios')


    context = {'form':form,'empleados':empleados,}

    return render(request, 'proyecto/DatosBancariosForm.html',context)

def BancariosUpdate(request, pk):

    item = DatosBancarios.objects.get(id=pk)

    if request.method == 'POST':
        form = BancariosUpdateForm(request.POST, instance=item)

        if form.is_valid():
            messages.success(request, f'Cambios guardados con éxito los datos bancarios de {item.status.perfil.nombres} {item.status.perfil.apellidos}')
            item = form.save(commit=False)
            item.save()
            return redirect('Tabla_datosbancarios')
    else:
        form = BancariosUpdateForm(instance=item)

    context = {'form':form,'item':item}

    return render(request, 'proyecto/Bancario_update.html',context)

def FormularioCosto(request):
    user_filter = UserDatos.objects.get(user=request.user)

    if user_filter.distrito.distrito == 'Matriz':
        empleados= Status.objects.filter(complete = True, complete_costo = False)
    else:
        perfil = Perfil.objects.filter(distrito = user_filter.distrito)
        empleados= Status.objects.filter(perfil__id__in=perfil.all(),complete = True, complete_costo = False)

    tablas= DatosISR.objects.all()
    #empleados= Status.objects.filter(complete= True, complete_costo = False)
    costo,created=Costo.objects.get_or_create(complete=False)
    form = CostoForm()
    puestos = Puesto.objects.all()

    #Constantes
    quincena=Decimal(14.00)
    mes=Decimal(30.40)
    impuesto_est=Decimal(0.0315)
    sar=Decimal(0.02)
    cesantia=Decimal(0.04625)
    infonavit=Decimal(0.05)
    comision=Decimal(0.09)


    if request.method == 'POST' and 'btnSend' in request.POST:
        form = CostoForm(request.POST,instance=costo)
        form.save(commit=False)

        if costo.amortizacion_infonavit < 0:
            messages.error(request, '(Amortización) La cantidad capturada debe ser mayor a 0')
        else:
            if costo.fonacot < 0:
                messages.error(request, '(Fonacot) La cantidad capturada debe ser mayor o igual 0')
            else:
                if costo.neto_catorcenal_sin_deducciones <= 0:
                    messages.error(request, '(Neto catorcenal) La cantidad capturada debe ser mayor a 0')
                else:
                    if costo.complemento_salario_catorcenal < 0:
                        messages.error(request, '(Complemento salario) La cantidad capturada debe ser mayor o igual 0')
                    else:
                        if costo.sueldo_diario <= 0:
                            messages.error(request, '(Sueldo diario) La cantidad capturada debe ser mayor a 0')
                        else:
                            if costo.sdi <= 0:
                                messages.error(request, '(SDI) La cantidad capturada debe ser mayor a 0')
                            else:
                                if costo.apoyo_de_pasajes < 0:
                                    messages.error(request, '(Apoyo pasajes) La cantidad capturada debe ser mayor o igual 0')
                                else:
                                    if costo.imms_obrero_patronal <= 0:
                                        messages.error(request, '(IMSS obrero) La cantidad capturada debe ser mayor a 0')
                                    else:
                                        if costo.apoyo_vist_familiar < 0:
                                            messages.error(request, '(Visita familiar) La cantidad capturada debe ser mayor o igual 0')
                                        else:
                                            if costo.estancia < 0:
                                                messages.error(request, '(Estancia) La cantidad capturada debe ser mayor o igual 0')
                                            else:
                                                if costo.renta < 0:
                                                    messages.error(request, '(Renta) La cantidad capturada debe ser mayor o igual 0')
                                                else:
                                                    if costo.apoyo_estudios < 0:
                                                        messages.error(request, '(Estudios) La cantidad capturada debe ser mayor o igual 0')
                                                    else:
                                                        if costo.amv < 0:
                                                            messages.error(request, '(AMV) La cantidad capturada debe ser mayor o igual 0')
                                                        else:
                                                            if costo.gasolina < 0:
                                                                messages.error(request, '(Gasolina) La cantidad capturada debe ser mayor o igual 0')
                                                            else:
                                                                if costo.campamento < 0:
                                                                    messages.error(request, '(Campamento) La cantidad capturada debe ser mayor o igual 0')
                                                                else:
                                                                    costo.total_deduccion = costo.amortizacion_infonavit + costo.fonacot
                                                                    costo.neto_pagar = costo.neto_catorcenal_sin_deducciones - costo.total_deduccion
                                                                    costo.sueldo_mensual_neto = (costo.neto_catorcenal_sin_deducciones/quincena)*mes
                                                                    costo.complemento_salario_mensual = (costo.complemento_salario_catorcenal/quincena)*mes
                                                                    costo.sueldo_mensual = costo.sueldo_diario*mes
                                                                    costo.sueldo_mensual_sdi = costo.sdi*mes
                                                                    costo.total_percepciones_mensual = costo.apoyo_de_pasajes + costo.sueldo_mensual
                                                                    for tabla in tablas:
                                                                        if costo.total_percepciones_mensual >= tabla.liminf:
                                                                            costo.lim_inferior = tabla.liminf
                                                                            costo.tasa=tabla.excedente
                                                                            costo.cuota_fija=tabla.cuota
                                                                        if costo.lim_inferior >= tabla.p_ingresos:
                                                                            costo.subsidio=tabla.subsidio
                                                                    costo.impuesto_estatal= costo.total_percepciones_mensual*impuesto_est
                                                                    costo.sar= costo.sueldo_mensual_sdi*sar
                                                                    costo.cesantia= costo.sueldo_mensual_sdi*cesantia
                                                                    costo.infonavit= costo.sueldo_mensual_sdi*infonavit
                                                                    costo.excedente= costo.total_percepciones_mensual - costo.lim_inferior
                                                                    costo.impuesto_marginal= costo.excedente * costo.tasa
                                                                    costo.impuesto= costo.impuesto_marginal + costo.cuota_fija
                                                                    costo.isr= costo.impuesto
                                                                    #dato.otros_bonos= dato.bonos.bonos_ct_ocho + dato.bonos.bonos_ct_nueve
                                                                    costo.total_apoyosbonos_empleadocomp= costo.apoyo_vist_familiar + costo.estancia + costo.renta + costo.apoyo_estudios + costo.amv + costo.campamento + costo.gasolina

                                                                    costo.total_apoyosbonos_agregcomis = costo.campamento #Modificar falta suma
                                                                    costo.comision_complemeto_salario_bonos= (costo.complemento_salario_mensual + costo.campamento)*comision #Falta suma dentro de la multiplicacion
                                                                    costo.total_costo_empresa = costo.sueldo_mensual_neto + costo.complemento_salario_mensual + costo.apoyo_de_pasajes + costo.impuesto_estatal + costo.imms_obrero_patronal + costo.sar + costo.cesantia + costo.infonavit + costo.isr + costo.total_apoyosbonos_empleadocomp #+ costo.total_apoyosbonos_agregcomis + costo.comision_complemeto_salario_bonos
                                                                    costo.ingreso_mensual_neto_empleado= costo.sueldo_mensual_neto + costo.complemento_salario_mensual + costo.apoyo_de_pasajes + costo.total_apoyosbonos_empleadocomp # + costo.total_apoyosbonos_agregcomis
                                                                    empleado = Status.objects.get(id = costo.status.id)
                                                                    #Debes dejar lo que este entre '' para que aparezca

                                                                    if form.is_valid():
                                                                        messages.success(request, 'Datos guardados con éxito')
                                                                        costo.complete=True
                                                                        empleado.complete_costo = True
                                                                        form.save()
                                                                        empleado.save()
                                                                        return redirect('Tabla_costo')


    context = {
        'form':form,
        'empleados':empleados,
        'puestos':puestos,
        'tablas':tablas,
        }

    return render(request, 'proyecto/CostoForm.html',context)

def CostoUpdate(request, pk):
    tablas= DatosISR.objects.all()
    costo = Costo.objects.get(id=pk)
    registros = costo.history.filter(~Q(amortizacion_infonavit = None))
    myfilter = Costo_historicFilter(request.GET, queryset=registros)
    registros=myfilter.qs
    puestos = Puesto.objects.all()

    comision=Decimal(0.09)

    #if costo.bonototal == None:
    #    costo.bonototal =0
    #else:
    #    costo.bonototal=costo.bonototal
    quincena=Decimal(14.00)
    mes=Decimal(30.40)
    impuesto_est=Decimal(0.0315)
    sar=Decimal(0.02)
    cesantia=Decimal(0.04625)
    infonavit=Decimal(0.05)
    if request.method == 'POST' and 'btnSend' in request.POST:
        form = CostoUpdateForm(request.POST, instance=costo)
        form.save(commit=False)

        if costo.amortizacion_infonavit < 0:
            messages.error(request, '(Amortización) La cantidad capturada debe ser mayor o igual 0')
        else:
            if costo.fonacot < 0:
                messages.error(request, '(Fonacot) La cantidad capturada debe ser mayor o igual 0')
            else:
                if costo.neto_catorcenal_sin_deducciones <= 0:
                    messages.error(request, '(Neto catorcenal) La cantidad capturada debe ser mayor a 0')
                else:
                    if costo.complemento_salario_catorcenal < 0:
                        messages.error(request, '(Complemento salario) La cantidad capturada debe ser mayor o igual 0')
                    else:
                        if costo.sueldo_diario <= 0:
                            messages.error(request, '(Sueldo diario) La cantidad capturada debe ser mayor a 0')
                        else:
                            if costo.sdi <= 0:
                                messages.error(request, '(SDI) La cantidad capturada debe ser mayor a 0')
                            else:
                                if costo.apoyo_de_pasajes < 0:
                                    messages.error(request, '(Apoyo pasajes) La cantidad capturada debe ser mayor o igual 0')
                                else:
                                    if costo.imms_obrero_patronal <= 0:
                                        messages.error(request, '(IMSS obrero) La cantidad capturada debe ser mayor a 0')
                                    else:
                                        if costo.apoyo_vist_familiar < 0:
                                            messages.error(request, '(Visita familiar) La cantidad capturada debe ser mayor o igual 0')
                                        else:
                                            if costo.estancia < 0:
                                                messages.error(request, '(Estancia) La cantidad capturada debe ser mayor o igual 0')
                                            else:
                                                if costo.renta < 0:
                                                    messages.error(request, '(Renta) La cantidad capturada debe ser mayor o igual 0')
                                                else:
                                                    if costo.apoyo_estudios < 0:
                                                        messages.error(request, '(Estudios) La cantidad capturada debe ser mayor o igual 0')
                                                    else:
                                                        if costo.amv < 0:
                                                            messages.error(request, '(AMV) La cantidad capturada debe ser mayor o igual 0')
                                                        else:
                                                            if costo.gasolina < 0:
                                                                messages.error(request, '(Gasolina) La cantidad capturada debe ser mayor o igual 0')
                                                            else:
                                                                if costo.campamento < 0:
                                                                    messages.error(request, '(Campamento) La cantidad capturada debe ser mayor o igual 0')
                                                                else:
                                                                    costo.total_deduccion = costo.amortizacion_infonavit + costo.fonacot
                                                                    costo.neto_pagar = costo.neto_catorcenal_sin_deducciones - costo.total_deduccion
                                                                    costo.sueldo_mensual_neto = (costo.neto_catorcenal_sin_deducciones/quincena)*mes
                                                                    costo.complemento_salario_mensual = (costo.complemento_salario_catorcenal/quincena)*mes
                                                                    costo.sueldo_mensual = costo.sueldo_diario*mes
                                                                    costo.sueldo_mensual_sdi = costo.sdi*mes
                                                                    costo.total_percepciones_mensual = costo.apoyo_de_pasajes + costo.sueldo_mensual
                                                                    for tabla in tablas:
                                                                        if costo.total_percepciones_mensual >= tabla.liminf:
                                                                            costo.lim_inferior = tabla.liminf
                                                                            costo.tasa=tabla.excedente
                                                                            costo.cuota_fija=tabla.cuota
                                                                        if costo.lim_inferior >= tabla.p_ingresos:
                                                                            costo.subsidio=tabla.subsidio
                                                                    costo.impuesto_estatal= costo.total_percepciones_mensual*impuesto_est
                                                                    costo.sar= costo.sueldo_mensual_sdi*sar
                                                                    costo.cesantia= costo.sueldo_mensual_sdi*cesantia
                                                                    costo.infonavit= costo.sueldo_mensual_sdi*infonavit
                                                                    costo.excedente= costo.total_percepciones_mensual - costo.lim_inferior
                                                                    costo.impuesto_marginal= costo.excedente * costo.tasa
                                                                    costo.impuesto= costo.impuesto_marginal + costo.cuota_fija
                                                                    costo.isr= costo.impuesto
                                                                    costo.total_apoyosbonos_empleadocomp= costo.apoyo_vist_familiar + costo.estancia + costo.renta + costo.apoyo_estudios + costo.amv + costo.campamento + costo.gasolina

                                                                    costo.total_apoyosbonos_agregcomis = costo.campamento #Modificar falta suma
                                                                    costo.comision_complemeto_salario_bonos= (costo.complemento_salario_mensual + costo.campamento)*comision #Falta suma dentro de la multiplicacion
                                                                    costo.total_costo_empresa = costo.sueldo_mensual_neto + costo.complemento_salario_mensual + costo.apoyo_de_pasajes + costo.impuesto_estatal + costo.imms_obrero_patronal + costo.sar + costo.cesantia + costo.infonavit + costo.isr + costo.total_apoyosbonos_empleadocomp #+ costo.total_apoyosbonos_agregcomis + costo.comision_complemeto_salario_bonos
                                                                    costo.ingreso_mensual_neto_empleado= costo.sueldo_mensual_neto + costo.complemento_salario_mensual + costo.apoyo_de_pasajes + costo.total_apoyosbonos_empleadocomp # + costo.total_apoyosbonos_agregcomis
                                                                    if form.is_valid():
                                                                        messages.success(request, f'Cambios guardados con éxito los costos de {costo.status.perfil.nombres} {costo.status.perfil.apellidos}')
                                                                        costo = form.save(commit=False)
                                                                        costo.save()
                                                                        return redirect('Tabla_costo')
    else:
        form = CostoUpdateForm(instance=costo)

    context = {'form':form,'costo':costo, 'registros':registros,'comision':comision,'myfilter':myfilter,'puestos':puestos}

    return render(request, 'proyecto/Costo_update.html',context)

def Costo_revisar(request, pk):

    costo = Costo.objects.get(id=pk)

    mes = datetime.date.today().month
    comision=Decimal(0.09)

    bonos_dato = Bonos.objects.filter(costo = costo).filter(fecha_bono__month = mes)
    sum_bonos = bonos_dato.aggregate(Sum('monto'))
    bonototal = sum_bonos['monto__sum']
    if bonototal == None:
        bonototal = 0
    costo.total_apoyosbonos_agregcomis = costo.campamento + bonototal
    costo.comision_complemeto_salario_bonos= (costo.complemento_salario_mensual + costo.campamento + bonototal)*comision #Falta suma dentro de la multiplicacion
    costo.total_costo_empresa = costo.sueldo_mensual_neto + costo.complemento_salario_mensual + costo.apoyo_de_pasajes + costo.impuesto_estatal + costo.imms_obrero_patronal + costo.sar + costo.cesantia + costo.infonavit + costo.isr + costo.total_apoyosbonos_empleadocomp + costo.total_apoyosbonos_agregcomis + costo.comision_complemeto_salario_bonos
    costo.ingreso_mensual_neto_empleado= costo.sueldo_mensual_neto + costo.complemento_salario_mensual + costo.apoyo_de_pasajes + costo.total_apoyosbonos_empleadocomp + costo.total_apoyosbonos_agregcomis

    costo.amortizacion_infonavit=locale.currency(costo.amortizacion_infonavit, grouping=True)
    costo.fonacot=locale.currency(costo.fonacot, grouping=True)
    costo.neto_catorcenal_sin_deducciones=locale.currency(costo.neto_catorcenal_sin_deducciones, grouping=True)
    costo.complemento_salario_catorcenal=locale.currency(costo.complemento_salario_catorcenal, grouping=True)
    costo.sueldo_diario=locale.currency(costo.sueldo_diario, grouping=True)
    costo.sdi=locale.currency(costo.sdi, grouping=True)
    costo.apoyo_de_pasajes=locale.currency(costo.apoyo_de_pasajes, grouping=True)
    costo.imms_obrero_patronal=locale.currency(costo.imms_obrero_patronal, grouping=True)
    costo.apoyo_vist_familiar=locale.currency(costo.apoyo_vist_familiar, grouping=True)
    costo.estancia=locale.currency(costo.estancia, grouping=True)
    costo.renta=locale.currency(costo.renta, grouping=True)
    costo.apoyo_estudios=locale.currency(costo.apoyo_estudios, grouping=True)
    costo.amv=locale.currency(costo.amv, grouping=True)
    costo.gasolina=locale.currency(costo.gasolina, grouping=True)
    costo.campamento=locale.currency(costo.campamento, grouping=True)
    costo.total_deduccion=locale.currency(costo.total_deduccion, grouping=True)
    costo.neto_pagar=locale.currency(costo.neto_pagar, grouping=True)
    costo.sueldo_mensual_neto=locale.currency(costo.sueldo_mensual_neto, grouping=True)
    costo.complemento_salario_mensual=locale.currency(costo.complemento_salario_mensual, grouping=True)
    costo.sueldo_mensual=locale.currency(costo.sueldo_mensual, grouping=True)
    costo.sueldo_mensual_sdi=locale.currency(costo.sueldo_mensual_sdi, grouping=True)
    costo.total_percepciones_mensual=locale.currency(costo.total_percepciones_mensual, grouping=True)
    costo.impuesto_estatal=locale.currency(costo.impuesto_estatal, grouping=True)
    costo.sar=locale.currency(costo.sar, grouping=True)
    costo.cesantia=locale.currency(costo.cesantia, grouping=True)
    costo.infonavit=locale.currency(costo.infonavit, grouping=True)
    costo.isr=locale.currency(costo.isr, grouping=True)
    costo.lim_inferior=locale.currency(costo.lim_inferior, grouping=True)
    costo.excedente =locale.currency(costo.excedente, grouping=True)
    costo.tasa=locale.currency(costo.tasa, grouping=True)
    costo.impuesto_marginal=locale.currency(costo.impuesto_marginal, grouping=True)
    costo.cuota_fija=locale.currency(costo.cuota_fija, grouping=True)
    costo.impuesto=locale.currency(costo.impuesto, grouping=True)
    costo.subsidio=locale.currency(costo.subsidio, grouping=True)
    costo.total_apoyosbonos_empleadocomp=locale.currency(costo.total_apoyosbonos_empleadocomp, grouping=True)
    if bonototal == None:
        costo.bonototal =locale.currency(0, grouping=True)
    else:
        costo.bonototal=locale.currency(bonototal, grouping=True)
    costo.total_apoyosbonos_agregcomis=locale.currency(costo.total_apoyosbonos_agregcomis, grouping=True)
    costo.comision_complemeto_salario_bonos=locale.currency(costo.comision_complemeto_salario_bonos, grouping=True)
    costo.total_costo_empresa=locale.currency(costo.total_costo_empresa, grouping=True)
    costo.ingreso_mensual_neto_empleado=locale.currency(costo.ingreso_mensual_neto_empleado, grouping=True)

    if request.method =='POST' and 'Pdf' in request.POST:
        return reporte_pdf_costo_detalles(costo)

    context = {'costo':costo,}

    return render(request, 'proyecto/Costo_revisar.html',context)

def TablaCosto(request):
    año = datetime.date.today().year

    user_filter = UserDatos.objects.get(user=request.user)

    if user_filter.distrito.distrito == 'Matriz':
        costos= Costo.objects.filter(complete=True,created_at__year=año).order_by("status__perfil__numero_de_trabajador")
    else:
        perfil = Perfil.objects.filter(distrito = user_filter.distrito,complete=True)
        costos = Costo.objects.filter(status__perfil__id__in=perfil.all(),created_at__year=año, complete=True).order_by("status__perfil__numero_de_trabajador")

    costo_filter = CostoFilter(request.GET, queryset=costos)
    costos = costo_filter.qs
    mes = datetime.date.today().month
    comision=Decimal(0.09)

    if request.method =='POST' and 'Excel' in request.POST:
        return convert_excel_costo(costos)


    for costo in costos:
        bonos_dato = Bonos.objects.filter(costo = costo).filter(fecha_bono__month = mes)
        sum_bonos = bonos_dato.aggregate(Sum('monto'))
        bonototal = sum_bonos['monto__sum']
        if bonototal == None:
            bonototal = 0
        costo.total_apoyosbonos_agregcomis = costo.campamento + bonototal
        costo.comision_complemeto_salario_bonos= (costo.complemento_salario_mensual + costo.campamento + bonototal)*comision #Falta suma dentro de la multiplicacion
        costo.total_costo_empresa = costo.sueldo_mensual_neto + costo.complemento_salario_mensual + costo.apoyo_de_pasajes + costo.impuesto_estatal + costo.imms_obrero_patronal + costo.sar + costo.cesantia + costo.infonavit + costo.isr + costo.total_apoyosbonos_empleadocomp + costo.total_apoyosbonos_agregcomis + costo.comision_complemeto_salario_bonos
        costo.ingreso_mensual_neto_empleado= costo.sueldo_mensual_neto + costo.complemento_salario_mensual + costo.apoyo_de_pasajes + costo.total_apoyosbonos_empleadocomp + costo.total_apoyosbonos_agregcomis

        costo.numero_de_trabajador=costo.status.perfil.numero_de_trabajador
        costo.empresa=costo.status.perfil.empresa
        costo.distrito=costo.status.perfil.distrito
        costo.proyecto=costo.status.perfil.proyecto
        costo.nombres=costo.status.perfil.nombres
        costo.apellidos=costo.status.perfil.apellidos
        costo.tipo_de_contrato=costo.status.tipo_de_contrato
        costo.puesto=costo.puesto

        costo.amortizacion_infonavit=locale.currency(costo.amortizacion_infonavit, grouping=True)
        costo.fonacot=locale.currency(costo.fonacot, grouping=True)
        costo.neto_catorcenal_sin_deducciones=locale.currency(costo.neto_catorcenal_sin_deducciones, grouping=True)
        costo.complemento_salario_catorcenal=locale.currency(costo.complemento_salario_catorcenal, grouping=True)
        costo.sueldo_diario=locale.currency(costo.sueldo_diario, grouping=True)
        costo.sdi=locale.currency(costo.sdi, grouping=True)
        costo.apoyo_de_pasajes=locale.currency(costo.apoyo_de_pasajes, grouping=True)
        costo.imms_obrero_patronal=locale.currency(costo.imms_obrero_patronal, grouping=True)
        costo.apoyo_vist_familiar=locale.currency(costo.apoyo_vist_familiar, grouping=True)
        costo.estancia=locale.currency(costo.estancia, grouping=True)
        costo.renta=locale.currency(costo.renta, grouping=True)
        costo.apoyo_estudios=locale.currency(costo.apoyo_estudios, grouping=True)
        costo.amv=locale.currency(costo.amv, grouping=True)
        costo.gasolina=locale.currency(costo.gasolina, grouping=True)
        costo.campamento=locale.currency(costo.campamento, grouping=True)
        costo.total_deduccion=locale.currency(costo.total_deduccion, grouping=True)
        costo.neto_pagar=locale.currency(costo.neto_pagar, grouping=True)
        costo.sueldo_mensual_neto=locale.currency(costo.sueldo_mensual_neto, grouping=True)
        costo.complemento_salario_mensual=locale.currency(costo.complemento_salario_mensual, grouping=True)
        costo.sueldo_mensual=locale.currency(costo.sueldo_mensual, grouping=True)
        costo.sueldo_mensual_sdi=locale.currency(costo.sueldo_mensual_sdi, grouping=True)
        costo.total_percepciones_mensual=locale.currency(costo.total_percepciones_mensual, grouping=True)
        costo.impuesto_estatal=locale.currency(costo.impuesto_estatal, grouping=True)
        costo.sar=locale.currency(costo.sar, grouping=True)
        costo.cesantia=locale.currency(costo.cesantia, grouping=True)
        costo.infonavit=locale.currency(costo.infonavit, grouping=True)
        costo.isr=locale.currency(costo.isr, grouping=True)
        costo.lim_inferior=locale.currency(costo.lim_inferior, grouping=True)
        costo.excedente=locale.currency(costo.excedente, grouping=True)
        costo.tasa=locale.currency(costo.tasa, grouping=True)
        costo.impuesto_marginal=locale.currency(costo.impuesto_marginal, grouping=True)
        costo.cuota_fija=locale.currency(costo.cuota_fija, grouping=True)
        costo.impuesto=locale.currency(costo.impuesto, grouping=True)
        costo.subsidio=locale.currency(costo.subsidio, grouping=True)
        costo.total_apoyosbonos_empleadocomp=locale.currency(costo.total_apoyosbonos_empleadocomp, grouping=True)
        costo.total_apoyosbonos_agregcomis=locale.currency(costo.total_apoyosbonos_agregcomis, grouping=True)
        costo.comision_complemeto_salario_bonos=locale.currency(costo.comision_complemeto_salario_bonos, grouping=True)
        costo.total_costo_empresa=locale.currency(costo.total_costo_empresa, grouping=True)
        costo.ingreso_mensual_neto_empleado=locale.currency(costo.ingreso_mensual_neto_empleado, grouping=True)

    context = {'costos':costos,'costo_filter':costo_filter,}

    return render(request, 'proyecto/Tabla_costo.html',context)

def TablaBonos(request):
    año = datetime.date.today().year
    user_filter = UserDatos.objects.get(user=request.user)

    if user_filter.distrito.distrito == 'Matriz':
        bonos= Bonos.objects.filter(complete=True,mes_bono__year=año).order_by("costo__status__perfil__numero_de_trabajador")
    else:
        perfil = Perfil.objects.filter(distrito = user_filter.distrito,complete=True)
        bonos = Bonos.objects.filter(costo__status__perfil__id__in=perfil.all(),mes_bono__year=año, complete=True).order_by("costo__status__perfil__numero_de_trabajador")

    bono_filter = BonosFilter(request.GET, queryset=bonos)
    bonos = bono_filter.qs

    if request.method =='POST' and 'Excel' in request.POST:
        return convert_excel_bonos(bonos)

    for bono in bonos:
        if bono.monto == None:
            bono.monto = 0
        else:
            bono.monto=locale.currency(bono.monto, grouping=True)
    context= {
        'bonos':bonos,
        'bono_filter':bono_filter,
        }

    return render(request, 'proyecto/BonosTabla.html',context)


def FormularioVacaciones(request):
    user_filter = UserDatos.objects.get(user=request.user)

    if user_filter.distrito.distrito == 'Matriz':
        empleados= Status.objects.filter(complete= True, complete_vacaciones = False)
    else:
        perfil = Perfil.objects.filter(distrito = user_filter.distrito)
        empleados= Status.objects.filter(perfil__id__in=perfil.all(),complete= True, complete_vacaciones = False)

    tablas= TablaVacaciones.objects.all()
    descanso,created=Vacaciones.objects.get_or_create(complete=False)
    form = VacacionesForm()

    periodo=1
    ahora = datetime.date.today()

    if request.method == 'POST' and 'btnSend' in request.POST:

        form = VacacionesForm(request.POST,instance=descanso)
        form.save(commit=False)
        #Aqui se busca el ultimo dato creado que en este caso es el año anterior y se le suma a los dias pendientes
        #if Vacaciones.objects.filter(status.id = descanso.status.id).last():
        #    pendientes = Vacaciones.objects.filter(status.id = descanso.status.id).last()
        #    pendientes = pendientes.total_pendiente
        #else:
        #    pendientes = 0

        descanso.dias_disfrutados = descanso.dias_disfrutados
        descanso.fecha_planta_anterior = descanso.status.fecha_planta_anterior
        descanso.fecha_planta = descanso.status.fecha_planta
        if descanso.fecha_planta_anterior:
            days = descanso.fecha_planta_anterior
        else:
            days = descanso.fecha_planta

        antiguedad = ahora.year - days.year
        if antiguedad <= periodo:
            antiguedad = periodo
        for tabla in tablas:
            if antiguedad >= tabla.years:
                descanso.dias_de_vacaciones = tabla.days
        #Aqui se agregan los dias pendientes anteriores
        descanso.dias_de_vacaciones = descanso.dias_de_vacaciones

        if descanso.dias_disfrutados < 0:
            messages.error(request, '(Dias disfrutados) La cantidad capturada debe ser mayor o igual 0')
        else:
            if descanso.dias_disfrutados > descanso.dias_de_vacaciones:
                messages.error(request, '(Dias disfrutados) La cantidad total capturada debe ser menor a {descanso.dias_de_vacaciones} ')
            else:
                periodofecha = descanso.created_at.year
                str(periodo)
                descanso.periodo=periodofecha
                descanso.total_pendiente=descanso.dias_de_vacaciones-descanso.dias_disfrutados

                empleado = Status.objects.get(id = descanso.status.id)
                if form.is_valid():
                    messages.success(request, 'Datos capturados con éxito')
                    descanso.complete=True
                    form.save()
                    empleado.complete_vacaciones = True
                    empleado.save()
                    return redirect('Tabla_vacaciones_empleados')


    context = {'form':form,'empleados':empleados}

    return render(request, 'proyecto/VacacionesForm.html',context)

def VacacionesUpdate(request, pk):
    tablas= TablaVacaciones.objects.all()
    descanso = Vacaciones.objects.get(id=pk)
    registros = descanso.history.filter(~Q(dias_disfrutados = None))
    trabajador = descanso.status
    descansos= Vacaciones.objects.filter(status=trabajador)
    periodo=1
    ahora = datetime.date.today()
    year = 365

    dias_anteriores = descanso.dias_disfrutados
    if request.method == 'POST':
        form = VacacionesUpdateForm(request.POST, instance=descanso)
        descanso = form.save(commit=False)
        #trabajador = descanso.status

        dias = descansos.aggregate(Sum('dias_disfrutados'))
        suma_dias = dias['dias_disfrutados__sum']
        if suma_dias == None:
            suma_dias =0
        dias_totales = descanso.dias_disfrutados + suma_dias
        descanso.dias_disfrutados = dias_totales

        descanso.fecha_planta_anterior = trabajador.fecha_planta_anterior
        descanso.fecha_planta = trabajador.fecha_planta

        if descanso.fecha_planta_anterior:
            days = descanso.fecha_planta_anterior
        else:
            days = descanso.fecha_planta
        antiguedad = ahora - days
        busqueda = antiguedad.days/year
        if busqueda <= periodo:
            busqueda = periodo
        for tabla in tablas:
            if busqueda >= tabla.years:
                descanso.dias_de_vacaciones = tabla.days
        if descanso.dias_disfrutados < 0 and descanso.dias_disfrutados:
            messages.error(request, '(Dias disfrutados) La cantidad capturada debe ser mayor a 0')
        else:
            if descanso.dias_disfrutados > descanso.dias_de_vacaciones:
                messages.error(request, f'(Dias disfrutados) La cantidad total capturada debe ser menor a {descanso.dias_de_vacaciones}, cantidad actual: {descanso.dias_disfrutados}')
            else:
                if descanso.dias_disfrutados <= dias_anteriores:
                    messages.error(request, 'No se puede ingresar un valor 0 o un valor negativo')
                else:
                    periodofecha = descanso.created_at.year
                    str(periodo)
                    descanso.periodo = periodofecha
                    descanso.total_pendiente = descanso.dias_de_vacaciones - dias_totales
                    if descanso.total_pendiente == None:
                        descanso.total_pendiente = 0
                    if form.is_valid():
                        messages.success(request, f'Cambios guardados con éxito los días de vacaciones de {descanso.status.perfil.nombres} {descanso.status.perfil.apellidos}')
                        form.save()
                        return redirect('Tabla_vacaciones_empleados')
    else:
        form = VacacionesUpdateForm()

    context = {
        'form':form,
        'descanso':descanso,
        'registros':registros,
        }

    return render(request, 'proyecto/Vacaciones_update.html',context)

def Tabla_Vacaciones(request): #Ya esta
#Aqui se quitan de las tablas los datos de las vacaciones anteriores, en el formulario se mandan a llamar para añadir los días pendientes

    año_actual = datetime.date.today().year
    fecha_inicio = date(año_actual, 1, 1)
    #año_anterior = fecha_inicio - timedelta(days=1)
    #año_anterior = año_anterior.year
    fecha_actual = datetime.date.today()
    if fecha_actual == fecha_inicio:
        datos = Vacaciones.objects.filter(complete = True)
        for dato in datos:
            if año_actual != dato.created_at.year:
                status = Status.objects.get(id = dato.status.id)
                status.complete_vacaciones = False
                status.save()

    user_filter = UserDatos.objects.get(user=request.user)

    if user_filter.distrito.distrito == 'Matriz':
        descansos= Vacaciones.objects.filter(complete=True,created_at__year=año_actual).annotate(Sum('dias_disfrutados')).order_by("status__perfil__numero_de_trabajador")
    else:
        perfil = Perfil.objects.filter(distrito = user_filter.distrito,complete=True)
        descansos = Vacaciones.objects.filter(status__perfil__id__in=perfil.all(), complete=True).annotate(Sum('dias_disfrutados')).order_by("status__perfil__numero_de_trabajador")

    vacaciones_filter = VacacionesFilter(request.GET, queryset=descansos)
    descansos = vacaciones_filter.qs
    if request.method =='POST' and 'Excel' in request.POST:
        return convert_excel_vacaciones(descansos)

    context= {
        'descansos':descansos,
        'vacaciones_filter':vacaciones_filter,
        }

    return render(request, 'proyecto/TablaVacaciones.html',context)

def FormularioEconomicos(request):
    user_filter = UserDatos.objects.get(user=request.user)

    if user_filter.distrito.distrito == 'Matriz':
        empleados= Status.objects.filter(complete= True, complete_economicos = False)
    else:
        perfil = Perfil.objects.filter(distrito = user_filter.distrito)
        empleados= Status.objects.filter(perfil__id__in=perfil.all(),complete= True, complete_economicos = False)

    #empleados= Status.objects.filter(complete= True, complete_economicos = False)
    economico,created=Economicos.objects.get_or_create(complete=False)
    form = EconomicosForm()
    total_dias_economicos=3
    dias_disfrutados=1

    if request.method == 'POST' and 'btnSend' in request.POST:
        form = EconomicosForm(request.POST,instance=economico)
        form.save(commit=False)
        #trabajador = economico.status
        #last_user = Economicos.objects.filter(status=trabajador).last()
        #dias = economicos.filter(status=trabajador).aggregate(Sum('dias_disfrutados'))
        #suma_dias = dias['dias_disfrutados__sum']
        #if suma_dias == None:
        #    suma_dias =0
        economico.dias_disfrutados = dias_disfrutados
        economico.dias_pendientes = total_dias_economicos - economico.dias_disfrutados
        periodo = economico.created_at.year
        str(periodo)
        economico.periodo=periodo
        #economico.dias_pendientes=total_dias_economicos-economico.dias_disfrutados
        empleado = Status.objects.get(id = economico.status.id)
        if form.is_valid():
            messages.success(request, 'Datos capturados con exíto')
            economico.complete=True
            economico.complete_dias=False
            empleado.complete_economicos = True
            form.save()
            empleado.save()
            return redirect('Tabla_economicos')

    context = {'form':form,'empleados':empleados,}

    return render(request, 'proyecto/EconomicosForm.html',context)

def EconomicosUpdate(request, pk):
    status = Status.objects.get(id=pk)
    economico,created=Economicos.objects.get_or_create(complete=False)
    form = EconomicosForm()
    total_dias_economicos=3
    dias_disfrutados=1

    if request.method == 'POST' and 'btnSend' in request.POST:
        form = EconomicosUpdateForm(request.POST,instance=economico)
        form.save(commit=False)
        last_economico = Economicos.objects.filter(status=status).last()
        economico.status=status
        economico.dias_disfrutados = dias_disfrutados + last_economico.dias_disfrutados
        economico.dias_pendientes = total_dias_economicos - economico.dias_disfrutados
        periodo = economico.created_at.year
        str(periodo)
        economico.periodo=periodo
        orden = Economicos.objects.filter(status = status.id).last()
        orden.complete_dias=True
        if economico.dias_disfrutados == total_dias_economicos:
            economico.complete_dias=True
        else:
            economico.complete_dias=False
        if form.is_valid():
            messages.success(request, 'Se capturaron con exíto los datos')
            economico.complete=True
            orden.save()
            form.save()
            return redirect('Tabla_economicos')

    context = {'form':form,'economico':economico,'status':status,}

    return render(request, 'proyecto/Economicos_update.html',context)

def Tabla_Economicos(request): #Ya esta
#Aqui se quitan de las tablas los datos de las economicos anteriores
    #empleado = Status.objects.get(id = descanso.status.id)
    año_actual = datetime.date.today().year
    dias_pendientes=3
    #fecha_inicio = date(año_actual, 1, 1)
    #año_anterior = fecha_inicio - timedelta(days=1)
    #año_anterior = año_anterior.year
    #fecha_actual = datetime.date.today()
    #if fecha_actual == fecha_inicio:
    #    datos = Economicos.objects.filter(complete = True)
    #    for dato in datos:
    #        if año_actual != dato.created_at.year:
    #            status = Status.objects.get(id = dato.status.id)
    #            status.complete_economicos = False
    #            status.save()
    user_filter = UserDatos.objects.get(user=request.user)

    if user_filter.distrito.distrito == 'Matriz':
        economicos= Economicos.objects.filter(complete=True,complete_dias=False,created_at__year=año_actual).order_by("status__perfil__numero_de_trabajador")
        #economicost= economicos.last()
        economicoss= Economicos.objects.filter(dias_pendientes=0,complete=True,complete_dias=True,created_at__year=año_actual).order_by("status__perfil__numero_de_trabajador")
    else:
        perfil = Perfil.objects.filter(distrito = user_filter.distrito,complete=True)
        economicos = Economicos.objects.filter(status__perfil__id__in=perfil.all(),complete=True,complete_dias=False,created_at__year=año_actual).annotate(Sum('dias_disfrutados')).order_by("status__perfil__numero_de_trabajador")
        #economicost = economicos.last()
        economicoss = Economicos.objects.filter(status__perfil__id__in=perfil.all(),complete=True,complete_dias=True,created_at__year=año_actual).annotate(Sum('dias_disfrutados')).order_by("status__perfil__numero_de_trabajador")
    #economicos= Economicos.objects.filter(complete=True).annotate(Sum('dias_disfrutados'))
    economico_filter = EconomicosFilter(request.GET, queryset=economicos)
    economicos = economico_filter.qs
    economico_filters = EconomicosFilter(request.GET, queryset=economicoss)
    economicoss = economico_filters.qs
    if request.method =='POST' and 'Excel' in request.POST:
        return convert_excel_economicos(economicos,economicoss)
    context= {
        'economicos':economicos,
        'economico_filter':economico_filter,
        'economicoss':economicoss,
        'economico_filters':economico_filters,
        }

    return render(request, 'proyecto/Tabla_economicos.html',context)

def EconomicosRevisar(request, pk):
    economicos = Economicos.objects.filter(status__id=pk)
    empleado = economicos.last()

    if request.method =='POST' and 'Pdf' in request.POST:
        return reporte_pdf_economico_detalles(economicos,empleado)

    context = {
        'empleado':empleado,
        'economicos':economicos,
        }

    return render(request, 'proyecto/Economicos_revisar.html',context)

def Tabla_Datosbancarios(request):
    user_filter = UserDatos.objects.get(user=request.user)

    if user_filter.distrito.distrito == 'Matriz':
        bancarios= DatosBancarios.objects.filter(complete=True).order_by("status__perfil__numero_de_trabajador")
    else:
        perfil = Perfil.objects.filter(distrito = user_filter.distrito,complete=True)
        bancarios = DatosBancarios.objects.filter(status__perfil__id__in=perfil.all(), complete=True).order_by("status__perfil__numero_de_trabajador")

    #bancarios= DatosBancarios.objects.filter(complete=True)
    bancario_filter = BancariosFilter(request.GET, queryset=bancarios)
    bancarios = bancario_filter.qs

    if request.method =='POST' and 'Excel' in request.POST:
        return convert_excel_bancarios(bancarios)

    context= {
        'bancarios':bancarios,
        'bancario_filter':bancario_filter,
        }

    return render(request, 'proyecto/Tabla_Datosbancarios.html',context)

def HistoryCosto(request, pk):
    costos = Costo.objects.get(id=pk)
    registros = costos.history.filter(~Q(amortizacion_infonavit = None))
    myfilter = Costo_historicFilter(request.GET, queryset=registros)
    registros=myfilter.qs
    if request.method == 'POST':

        costo.impuesto_estatal=locale.currency(costo.impuesto_estatal, grouping=True)
        costo.sar=locale.currency(costo.sar, grouping=True)
        costo.cesantia=locale.currency(costo.cesantia, grouping=True)
        costo.infonavit=locale.currency(costo.infonavit, grouping=True)
        costo.isr=locale.currency(costo.isr, grouping=True)



    context = {'costos':costos, 'registros':registros,'myfilter':myfilter,}

    return render(request, 'proyecto/Costo_history.html',context)

def convert_excel_costo(bancario):
    response= HttpResponse(content_type = "application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename = Reporte_costos_' + str(datetime.date.today())+'.xlsx'
    wb = Workbook()
    ws = wb.create_sheet(title='Reporte')
    #Comenzar en la fila 1
    row_num = 1

    #Create heading style and adding to workbook | Crear el estilo del encabezado y agregarlo al Workbook
    head_style = NamedStyle(name = "head_style")
    head_style.font = Font(name = 'Arial', color = '00FFFFFF', bold = True, size = 11)
    head_style.fill = PatternFill("solid", fgColor = '00003366')
    wb.add_named_style(head_style)
    #Create body style and adding to workbook
    body_style = NamedStyle(name = "body_style")
    body_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(body_style)
    #Create messages style and adding to workbook
    messages_style = NamedStyle(name = "mensajes_style")
    messages_style.font = Font(name="Arial Narrow", size = 11)
    wb.add_named_style(messages_style)
    #Create date style and adding to workbook
    date_style = NamedStyle(name='date_style', number_format='DD/MM/YYYY')
    date_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(date_style)
    money_style = NamedStyle(name='money_style', number_format='$ #,##0.00')
    money_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(money_style)
    money_resumen_style = NamedStyle(name='money_resumen_style', number_format='$ #,##0.00')
    money_resumen_style.font = Font(name ='Calibri', size = 14, bold = True)
    wb.add_named_style(money_resumen_style)

    columns = ['Empresa','Distrito','Proyecto','Subproyecto','Nombre','Puesto','Complemento Salario Catorcenal', 'Apoyo de Pasajes','Total percepciones mensual',
                'Impuesto Estatal','IMSS obrero patronal','SAR 2%', 'Cesantía','Infonavit','ISR','Apoyo Visita Familiar','Apoyo Estancia','Apoyo Renta',
                'Apoyo de Estudios','Apoyo de Mantto Vehicular','Gasolina','Total apoyos y bonos','Total costo mensual para la empresa','Ingreso mensual neto del empleado']

    for col_num in range(len(columns)):
        (ws.cell(row = row_num, column = col_num+1, value=columns[col_num])).style = head_style
        if col_num < 4:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 10
        if col_num == 4:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 30
        else:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 15


    columna_max = len(columns)+2

    (ws.cell(column = columna_max, row = 1, value='{Reporte Creado Automáticamente por Savia RH. UH}')).style = messages_style
    (ws.cell(column = columna_max, row = 2, value='{Software desarrollado por Vordcab S.A. de C.V.}')).style = messages_style
    (ws.cell(column = columna_max, row = 3, value='Algún dato')).style = messages_style
    (ws.cell(column = columna_max +1, row=3, value = 'alguna sumatoria')).style = money_resumen_style
    ws.column_dimensions[get_column_letter(columna_max)].width = 20
    ws.column_dimensions[get_column_letter(columna_max + 1)].width = 20

    rows = bancario.values_list('status__perfil__empresa__empresa','status__perfil__distrito__distrito','status__perfil__proyecto','status__perfil__subproyecto',Concat('status__perfil__nombres',Value(' '),'status__perfil__apellidos'), 'puesto','complemento_salario_catorcenal',
                            'apoyo_de_pasajes','total_percepciones_mensual','impuesto_estatal','imms_obrero_patronal','sar','cesantia','infonavit','isr','apoyo_vist_familiar','estancia','renta',
                            'apoyo_estudios','amv','gasolina','total_apoyosbonos_agregcomis','total_costo_empresa','ingreso_mensual_neto_empleado')


    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if col_num <= 5:
                (ws.cell(row = row_num, column = col_num+1, value=row[col_num])).style = body_style
            if col_num > 5 and col_num <=23:
                (ws.cell(row = row_num, column = col_num+1, value=row[col_num])).style = money_style
            else:
                (ws.cell(row = row_num, column = col_num+1, value=str(row[col_num]))).style = body_style

    sheet = wb['Sheet']
    wb.remove(sheet)
    wb.save(response)

    return(response)

def convert_excel_bancarios(bancarios):
    response= HttpResponse(content_type = "application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename = Reporte_datos_bancarios_' + str(datetime.date.today())+'.xlsx'
    wb = Workbook()
    ws = wb.create_sheet(title='Reporte')
    #Comenzar en la fila 1
    row_num = 1

    #Create heading style and adding to workbook | Crear el estilo del encabezado y agregarlo al Workbook
    head_style = NamedStyle(name = "head_style")
    head_style.font = Font(name = 'Arial', color = '00FFFFFF', bold = True, size = 11)
    head_style.fill = PatternFill("solid", fgColor = '00003366')
    wb.add_named_style(head_style)
    #Create body style and adding to workbook
    body_style = NamedStyle(name = "body_style")
    body_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(body_style)
    #Create messages style and adding to workbook
    messages_style = NamedStyle(name = "mensajes_style")
    messages_style.font = Font(name="Arial Narrow", size = 11)
    wb.add_named_style(messages_style)
    #Create date style and adding to workbook
    date_style = NamedStyle(name='date_style', number_format='DD/MM/YYYY')
    date_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(date_style)
    money_style = NamedStyle(name='money_style', number_format='$ #,##0.00')
    money_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(money_style)
    money_resumen_style = NamedStyle(name='money_resumen_style', number_format='$ #,##0.00')
    money_resumen_style.font = Font(name ='Calibri', size = 14, bold = True)
    wb.add_named_style(money_resumen_style)

    columns = ['Empresa','Distrito','Nombre','No. de cuenta','No. de tarjeta','Clabe interbancaria','Banco']

    for col_num in range(len(columns)):
        (ws.cell(row = row_num, column = col_num+1, value=columns[col_num])).style = head_style
        if col_num < 4:
            ws.column_dimensions[get_column_letter(col_num + 2)].width = 10
        if col_num == 4:
            ws.column_dimensions[get_column_letter(col_num + 2)].width = 30
        else:
            ws.column_dimensions[get_column_letter(col_num + 2)].width = 15


    columna_max = len(columns)+2

    (ws.cell(column = columna_max, row = 1, value='{Reporte Creado Automáticamente por Savia RH. UH}')).style = messages_style
    (ws.cell(column = columna_max, row = 2, value='{Software desarrollado por Vordcab S.A. de C.V.}')).style = messages_style
    (ws.cell(column = columna_max, row = 3, value='Algún dato')).style = messages_style
    (ws.cell(column = columna_max +1, row=3, value = 'alguna sumatoria')).style = money_resumen_style
    ws.column_dimensions[get_column_letter(columna_max)].width = 20
    ws.column_dimensions[get_column_letter(columna_max + 1)].width = 20

    rows = bancarios.values_list('status__perfil__empresa__empresa','status__perfil__distrito__distrito',Concat('status__perfil__nombres',Value(' '),
                                'status__perfil__apellidos'),'no_de_cuenta','numero_de_tarjeta','clabe_interbancaria','banco')


    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if col_num <= 8:
                (ws.cell(row = row_num, column = col_num+1, value=row[col_num])).style = body_style

    sheet = wb['Sheet']
    wb.remove(sheet)
    wb.save(response)

    return(response)

def convert_excel_bonos(bonos):
    response= HttpResponse(content_type = "application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename = Reporte_bonos_' + str(datetime.date.today())+'.xlsx'
    wb = Workbook()
    ws = wb.create_sheet(title='Reporte')
    #Comenzar en la fila 1
    row_num = 1

    #Create heading style and adding to workbook | Crear el estilo del encabezado y agregarlo al Workbook
    head_style = NamedStyle(name = "head_style")
    head_style.font = Font(name = 'Arial', color = '00FFFFFF', bold = True, size = 11)
    head_style.fill = PatternFill("solid", fgColor = '00003366')
    wb.add_named_style(head_style)
    #Create body style and adding to workbook
    body_style = NamedStyle(name = "body_style")
    body_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(body_style)
    #Create messages style and adding to workbook
    messages_style = NamedStyle(name = "mensajes_style")
    messages_style.font = Font(name="Arial Narrow", size = 11)
    wb.add_named_style(messages_style)
    #Create date style and adding to workbook
    date_style = NamedStyle(name='date_style', number_format='DD/MM/YYYY')
    date_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(date_style)
    money_style = NamedStyle(name='money_style', number_format='$ #,##0.00')
    money_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(money_style)
    money_resumen_style = NamedStyle(name='money_resumen_style', number_format='$ #,##0.00')
    money_resumen_style.font = Font(name ='Calibri', size = 14, bold = True)
    wb.add_named_style(money_resumen_style)

    columns = ['Empresa','Distrito','Nombre','No. de cuenta','No. de tarjeta','Clabe interbancaria',
                'Banco','Fecha del bono','Bono total',]

    for col_num in range(len(columns)):
        (ws.cell(row = row_num, column = col_num+1, value=columns[col_num])).style = head_style
        if col_num < 4:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 10
        if col_num == 4:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 30
        else:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 15


    columna_max = len(columns)+2

    (ws.cell(column = columna_max, row = 1, value='{Reporte Creado Automáticamente por Savia RH. UH}')).style = messages_style
    (ws.cell(column = columna_max, row = 2, value='{Software desarrollado por Vordcab S.A. de C.V.}')).style = messages_style
    (ws.cell(column = columna_max, row = 3, value='Algún dato')).style = messages_style
    (ws.cell(column = columna_max +1, row=3, value = 'alguna sumatoria')).style = money_resumen_style
    ws.column_dimensions[get_column_letter(columna_max)].width = 20
    ws.column_dimensions[get_column_letter(columna_max + 1)].width = 20

    rows = bonos.values_list('costo__status__perfil__empresa__empresa','costo__status__perfil__distrito__distrito',Concat('costo__status__perfil__nombres',Value(' '),
                            'costo__status__perfil__apellidos'),'datosbancarios__no_de_cuenta','datosbancarios__numero_de_tarjeta',
                            'datosbancarios__clabe_interbancaria','datosbancarios__banco','fecha_bono','monto',)


    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if col_num < 7:
                (ws.cell(row = row_num, column = col_num+1, value=row[col_num])).style = body_style
            if col_num == 7:
                (ws.cell(row = row_num, column = col_num+1, value=row[col_num])).style = date_style
            if col_num == 8:
                (ws.cell(row = row_num, column = col_num+1, value=row[col_num])).style = money_style

    sheet = wb['Sheet']
    wb.remove(sheet)
    wb.save(response)

    return(response)

def convert_excel_vacaciones(descansos):
    response= HttpResponse(content_type = "application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename = Reporte_vacaciones_' + str(datetime.date.today())+'.xlsx'
    wb = Workbook()
    ws = wb.create_sheet(title='Reporte')
    #Comenzar en la fila 1
    row_num = 1

    #Create heading style and adding to workbook | Crear el estilo del encabezado y agregarlo al Workbook
    head_style = NamedStyle(name = "head_style")
    head_style.font = Font(name = 'Arial', color = '00FFFFFF', bold = True, size = 11)
    head_style.fill = PatternFill("solid", fgColor = '00003366')
    wb.add_named_style(head_style)
    #Create body style and adding to workbook
    body_style = NamedStyle(name = "body_style")
    body_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(body_style)
    #Create messages style and adding to workbook
    messages_style = NamedStyle(name = "mensajes_style")
    messages_style.font = Font(name="Arial Narrow", size = 11)
    wb.add_named_style(messages_style)
    #Create date style and adding to workbook
    date_style = NamedStyle(name='date_style', number_format='DD/MM/YYYY')
    date_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(date_style)
    money_style = NamedStyle(name='money_style', number_format='$ #,##0.00')
    money_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(money_style)
    money_resumen_style = NamedStyle(name='money_resumen_style', number_format='$ #,##0.00')
    money_resumen_style.font = Font(name ='Calibri', size = 14, bold = True)
    wb.add_named_style(money_resumen_style)

    columns = ['Empresa','Distrito','Nombre','Fecha de planta anterior','Fecha de planta','Periodo vacacional','Días de vacaciones',
                'Días disfrutados y/o pagados','Total pendiente','Comentario',]

    for col_num in range(len(columns)):
        (ws.cell(row = row_num, column = col_num+1, value=columns[col_num])).style = head_style
        if col_num < 4:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 10
        if col_num == 4:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 30
        else:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 15


    columna_max = len(columns)+2

    (ws.cell(column = columna_max, row = 1, value='{Reporte Creado Automáticamente por Savia RH. UH}')).style = messages_style
    (ws.cell(column = columna_max, row = 2, value='{Software desarrollado por Vordcab S.A. de C.V.}')).style = messages_style
    (ws.cell(column = columna_max, row = 3, value='Algún dato')).style = messages_style
    (ws.cell(column = columna_max +1, row=3, value = 'alguna sumatoria')).style = money_resumen_style
    ws.column_dimensions[get_column_letter(columna_max)].width = 20
    ws.column_dimensions[get_column_letter(columna_max + 1)].width = 20

    rows = descansos.values_list('status__perfil__empresa__empresa','status__perfil__distrito__distrito',Concat('status__perfil__nombres',Value(' '),
                            'status__perfil__apellidos'),'status__fecha_planta_anterior','status__fecha_planta','periodo','dias_de_vacaciones',
                            'dias_disfrutados','total_pendiente','comentario')


    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if col_num < 3:
                (ws.cell(row = row_num, column = col_num+1, value=row[col_num])).style = body_style
            if col_num > 3:
                (ws.cell(row = row_num, column = col_num+1, value=row[col_num])).style = date_style
            if col_num >5:
                (ws.cell(row = row_num, column = col_num+1, value=row[col_num])).style = body_style
    sheet = wb['Sheet']
    wb.remove(sheet)
    wb.save(response)

    return(response)

def convert_excel_uniformes(ropas):
    response= HttpResponse(content_type = "application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename = Reporte_uniformes_' + str(datetime.date.today())+'.xlsx'
    wb = Workbook()
    ws = wb.create_sheet(title='Reporte')
    #Comenzar en la fila 1
    row_num = 1

    #Create heading style and adding to workbook | Crear el estilo del encabezado y agregarlo al Workbook
    head_style = NamedStyle(name = "head_style")
    head_style.font = Font(name = 'Arial', color = '00FFFFFF', bold = True, size = 11)
    head_style.fill = PatternFill("solid", fgColor = '00003366')
    wb.add_named_style(head_style)
    #Create body style and adding to workbook
    body_style = NamedStyle(name = "body_style")
    body_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(body_style)
    #Create messages style and adding to workbook
    messages_style = NamedStyle(name = "mensajes_style")
    messages_style.font = Font(name="Arial Narrow", size = 11)
    wb.add_named_style(messages_style)
    #Create date style and adding to workbook
    date_style = NamedStyle(name='date_style', number_format='DD/MM/YYYY')
    date_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(date_style)
    money_style = NamedStyle(name='money_style', number_format='$ #,##0.00')
    money_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(money_style)
    money_resumen_style = NamedStyle(name='money_resumen_style', number_format='$ #,##0.00')
    money_resumen_style.font = Font(name ='Calibri', size = 14, bold = True)
    wb.add_named_style(money_resumen_style)

    columns = ['Empresa','Distrito','Nombre','Fecha de ultima entrega','Uniformes entregados','Camisola','Pantalon','Camisa administrativa blanca',
                'Camisa administrativa azul','Camisa administrativa beige','Playera polo','Overol','Botas',]

    for col_num in range(len(columns)):
        (ws.cell(row = row_num, column = col_num+1, value=columns[col_num])).style = head_style
        if col_num < 4:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 10
        if col_num == 4:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 30
        else:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 15


    columna_max = len(columns)+2

    (ws.cell(column = columna_max, row = 1, value='{Reporte Creado Automáticamente por Savia RH. UH}')).style = messages_style
    (ws.cell(column = columna_max, row = 2, value='{Software desarrollado por Vordcab S.A. de C.V.}')).style = messages_style
    (ws.cell(column = columna_max, row = 3, value='Algún dato')).style = messages_style
    (ws.cell(column = columna_max +1, row=3, value = 'alguna sumatoria')).style = money_resumen_style
    ws.column_dimensions[get_column_letter(columna_max)].width = 20
    ws.column_dimensions[get_column_letter(columna_max + 1)].width = 20

    rows = ropas.values_list('status__perfil__empresa__empresa','status__perfil__distrito__distrito',Concat('status__perfil__nombres',Value(' '),
                            'status__perfil__apellidos'),'fecha_ultima_entrega','uniformes_entregados','camisola','pantalon','camisa_blanca','camisa_azul',
                            'camisa_beige','playera_polo','overol','botas',)


    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if col_num < 3:
                (ws.cell(row = row_num, column = col_num+1, value=row[col_num])).style = body_style
            if col_num == 3:
                (ws.cell(row = row_num, column = col_num+1, value=row[col_num])).style = date_style
            if col_num > 3:
                (ws.cell(row = row_num, column = col_num+1, value=row[col_num])).style = body_style


    sheet = wb['Sheet']
    wb.remove(sheet)
    wb.save(response)

    return(response)

def convert_excel_economicos(economicos,economicoss):
    response= HttpResponse(content_type = "application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename = Reporte_días_economicos_' + str(datetime.date.today())+'.xlsx'
    wb = Workbook()
    ws = wb.create_sheet(title='Reporte')
    #Comenzar en la fila 1
    row_num = 1

    #Create heading style and adding to workbook | Crear el estilo del encabezado y agregarlo al Workbook
    head_style = NamedStyle(name = "head_style")
    head_style.font = Font(name = 'Arial', color = '00FFFFFF', bold = True, size = 11)
    head_style.fill = PatternFill("solid", fgColor = '00003366')
    wb.add_named_style(head_style)
    #Create body style and adding to workbook
    body_style = NamedStyle(name = "body_style")
    body_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(body_style)
    #Create messages style and adding to workbook
    messages_style = NamedStyle(name = "mensajes_style")
    messages_style.font = Font(name="Arial Narrow", size = 11)
    wb.add_named_style(messages_style)
    #Create date style and adding to workbook
    date_style = NamedStyle(name='date_style', number_format='DD/MM/YYYY')
    date_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(date_style)
    money_style = NamedStyle(name='money_style', number_format='$ #,##0.00')
    money_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(money_style)
    money_resumen_style = NamedStyle(name='money_resumen_style', number_format='$ #,##0.00')
    money_resumen_style.font = Font(name ='Calibri', size = 14, bold = True)
    wb.add_named_style(money_resumen_style)

    columns = ['Empresa','Distrito','Nombre','Días económicos disfrutados','Días económicos pendientes',]

    for col_num in range(len(columns)):
        (ws.cell(row = row_num, column = col_num+1, value=columns[col_num])).style = head_style
        if col_num < 4:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 10
        if col_num == 4:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 30
        else:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 15


    columna_max = len(columns)+2

    (ws.cell(column = columna_max, row = 1, value='{Reporte Creado Automáticamente por Savia RH. UH}')).style = messages_style
    (ws.cell(column = columna_max, row = 2, value='{Software desarrollado por Vordcab S.A. de C.V.}')).style = messages_style
    (ws.cell(column = columna_max, row = 3, value='Algún dato')).style = messages_style
    (ws.cell(column = columna_max +1, row=3, value = 'alguna sumatoria')).style = money_resumen_style
    ws.column_dimensions[get_column_letter(columna_max)].width = 20
    ws.column_dimensions[get_column_letter(columna_max + 1)].width = 20

    rows = economicos.values_list('status__perfil__empresa__empresa','status__perfil__distrito__distrito',Concat('status__perfil__nombres',Value(' '),
                            'status__perfil__apellidos'),'dias_disfrutados','dias_pendientes',)
    rows2 = economicoss.values_list('status__perfil__empresa__empresa','status__perfil__distrito__distrito',Concat('status__perfil__nombres',Value(' '),
                            'status__perfil__apellidos'),'dias_disfrutados','dias_pendientes',)

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if col_num <= 5:
                (ws.cell(row = row_num, column = col_num+1, value=row[col_num])).style = body_style
    for row in rows2:
        row_num += 1
        for col_num in range(len(row)):
            if col_num <= 5:
                (ws.cell(row = row_num, column = col_num+1, value=row[col_num])).style = body_style

    sheet = wb['Sheet']
    wb.remove(sheet)
    wb.save(response)

    return(response)

def convert_excel_perfil(perfiles):
    response= HttpResponse(content_type = "application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename = Reporte_empleados_' + str(datetime.date.today())+'.xlsx'
    wb = Workbook()
    ws = wb.create_sheet(title='Reporte')
    #Comenzar en la fila 1
    row_num = 1

    #Create heading style and adding to workbook | Crear el estilo del encabezado y agregarlo al Workbook
    head_style = NamedStyle(name = "head_style")
    head_style.font = Font(name = 'Arial', color = '00FFFFFF', bold = True, size = 11)
    head_style.fill = PatternFill("solid", fgColor = '00003366')
    wb.add_named_style(head_style)
    #Create body style and adding to workbook
    body_style = NamedStyle(name = "body_style")
    body_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(body_style)
    #Create messages style and adding to workbook
    messages_style = NamedStyle(name = "mensajes_style")
    messages_style.font = Font(name="Arial Narrow", size = 11)
    wb.add_named_style(messages_style)
    #Create date style and adding to workbook
    date_style = NamedStyle(name='date_style', number_format='DD/MM/YYYY')
    date_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(date_style)
    money_style = NamedStyle(name='money_style', number_format='$ #,##0.00')
    money_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(money_style)
    money_resumen_style = NamedStyle(name='money_resumen_style', number_format='$ #,##0.00')
    money_resumen_style.font = Font(name ='Calibri', size = 14, bold = True)
    wb.add_named_style(money_resumen_style)

    columns = ['Nombre','Número de trabajador','Empresa','Distrito','Fecha de nacimiento','Correo electrónico','Proyecto','Subproyecto',]

    for col_num in range(len(columns)):
        (ws.cell(row = row_num, column = col_num+1, value=columns[col_num])).style = head_style
        if col_num == 0:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 30
        elif col_num > 0 and col_num < 5:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 12
        elif col_num > 4 and col_num < 7:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 25
        else:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 10


    columna_max = len(columns)+2

    (ws.cell(column = columna_max, row = 1, value='{Reporte Creado Automáticamente por Savia RH. UH}')).style = messages_style
    (ws.cell(column = columna_max, row = 2, value='{Software desarrollado por Vordcab S.A. de C.V.}')).style = messages_style
    (ws.cell(column = columna_max, row = 3, value='Empleados:')).style = messages_style

    ws.column_dimensions[get_column_letter(columna_max)].width = 20
    ws.column_dimensions[get_column_letter(columna_max + 1)].width = 20

    rows = perfiles.values_list(Concat('nombres',Value(' '),'apellidos'),'numero_de_trabajador','empresa__empresa','distrito__distrito',
                                        'fecha_nacimiento','correo_electronico','proyecto__proyecto','subproyecto__subproyecto',)


    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if col_num < 4:
                (ws.cell(row = row_num, column = col_num+1, value=row[col_num])).style = body_style
            if col_num == 4:
                (ws.cell(row = row_num, column = col_num+1, value=row[col_num])).style = date_style
            if col_num > 4:
                (ws.cell(row = row_num, column = col_num+1, value=row[col_num])).style = body_style

    (ws.cell(column = columna_max +1, row=3, value = row_num - 1)).style = messages_style

    sheet = wb['Sheet']
    wb.remove(sheet)
    wb.save(response)

    return(response)

def convert_excel_status(status):
    response= HttpResponse(content_type = "application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename = Reporte_empleados_status_' + str(datetime.date.today())+'.xlsx'
    wb = Workbook()
    ws = wb.create_sheet(title='Reporte')
    #Comenzar en la fila 1
    row_num = 1

    #Create heading style and adding to workbook | Crear el estilo del encabezado y agregarlo al Workbook
    head_style = NamedStyle(name = "head_style")
    head_style.font = Font(name = 'Arial', color = '00FFFFFF', bold = True, size = 11)
    head_style.fill = PatternFill("solid", fgColor = '00003366')
    wb.add_named_style(head_style)
    #Create body style and adding to workbook
    body_style = NamedStyle(name = "body_style")
    body_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(body_style)
    #Create messages style and adding to workbook
    messages_style = NamedStyle(name = "mensajes_style")
    messages_style.font = Font(name="Arial Narrow", size = 11)
    wb.add_named_style(messages_style)
    #Create date style and adding to workbook
    date_style = NamedStyle(name='date_style', number_format='DD/MM/YYYY')
    date_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(date_style)
    money_style = NamedStyle(name='money_style', number_format='$ #,##0.00')
    money_style.font = Font(name ='Calibri', size = 10)
    wb.add_named_style(money_style)
    money_resumen_style = NamedStyle(name='money_resumen_style', number_format='$ #,##0.00')
    money_resumen_style.font = Font(name ='Calibri', size = 14, bold = True)
    wb.add_named_style(money_resumen_style)

    columns = ['Nombre','Registro patronal','NSS','CURP','RFC','Profesión','No. de cédula','Nivel del empleado','Tipo de contrato','Último contrato vence',
                'Tipo de sangre','Género','Teléfono','Domicilio','Estado civil','Fecha de planta anterior','Fecha de planta actual',]

    for col_num in range(len(columns)):
        (ws.cell(row = row_num, column = col_num+1, value=columns[col_num])).style = head_style
        if col_num == 0:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 30
        elif col_num>0 and col_num < 3 and col_num > 3 and col_num < 13:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 15
        elif col_num == 3:
             ws.column_dimensions[get_column_letter(col_num + 1)].width = 20
        elif col_num == 13:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 30
        else:
            ws.column_dimensions[get_column_letter(col_num + 1)].width = 15


    columna_max = len(columns)+2

    (ws.cell(column = columna_max, row = 1, value='{Reporte Creado Automáticamente por Savia RH. UH}')).style = messages_style
    (ws.cell(column = columna_max, row = 2, value='{Software desarrollado por Vordcab S.A. de C.V.}')).style = messages_style
    (ws.cell(column = columna_max, row = 3, value='Empleados:')).style = messages_style

    ws.column_dimensions[get_column_letter(columna_max)].width = 20
    ws.column_dimensions[get_column_letter(columna_max + 1)].width = 20

    rows = status.values_list(Concat('perfil__nombres',Value(' '),'perfil__apellidos'),'registro_patronal__patronal','nss','curp','rfc','profesion','no_cedula',
                                        'nivel','tipo_de_contrato__contrato','ultimo_contrato_vence','tipo_sangre__sangre','sexo__sexo','telefono','domicilio','estado_civil__estado_civil',
                                        'fecha_planta_anterior','fecha_planta',)


    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if col_num < 9:
                (ws.cell(row = row_num, column = col_num+1, value=row[col_num])).style = body_style
            if col_num == 9:
                (ws.cell(row = row_num, column = col_num+1, value=row[col_num])).style = date_style
            if col_num > 9:
                (ws.cell(row = row_num, column = col_num+1, value=row[col_num])).style = body_style
            if col_num >= 15:
                (ws.cell(row = row_num, column = col_num+1, value=row[col_num])).style = date_style

    (ws.cell(column = columna_max +1, row=3, value = row_num-1)).style = messages_style

    sheet = wb['Sheet']
    wb.remove(sheet)
    wb.save(response)

    return(response)


def upload_batch_empleados(request):

    form = Empleados_BatchForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        form = Empleados_BatchForm()
        empleados_list = Empleados_Batch.objects.get(activated = False)
        f = open(empleados_list.file_name.path, 'r')
        reader = csv.reader(f)
        next(reader) #Advance past the reader

        for row in reader:
            fecha=datetime.datetime.strptime(row[5], "%d/%m/%Y").date()
            #if Perfil.objects.get(numero_de_trabajador != row[0]):
            if Perfil.objects.filter(numero_de_trabajador = row[0]):
                messages.error(request,f'El perfil del empleado #{row[0]} ya existe dentro de la base de datos')
            else:
                if Empresa.objects.filter(empresa = row[1]):
                    empresa = Empresa.objects.get(empresa = row[1])
                    if Distrito.objects.filter(distrito = row[2]):
                        distrito = Distrito.objects.get(distrito = row[2])
                        if Proyecto.objects.filter(proyecto = row[7]):
                            proyecto = Proyecto.objects.get(proyecto = row[7])
                            if SubProyecto.objects.filter(subproyecto = row[8]):
                                subproyecto = SubProyecto.objects.get(subproyecto = row[8])
                                empleado = Perfil(numero_de_trabajador=row[0], empresa=empresa, distrito=distrito, nombres=row[3],
                                    apellidos=row[4],fecha_nacimiento=fecha,correo_electronico=row[6],proyecto=proyecto,subproyecto=subproyecto,
                                    complete=True, complete_status=False,)

                                empleado.save()
                            else:
                                messages.error(request,f'El subproyecto no existe dentro de la base de datos, empleado #{row[0]}')
                        else:
                            messages.error(request,f'El proyecto no existe dentro de la base de datos, empleado #{row[0]}')
                    else:
                        messages.error(request,f'El distrito no existe dentro de la base de datos, empleado #{row[0]}')
                else:
                    messages.error(request,f'La empresa no existe dentro de la base de datos, empleado #{row[0]}')
        empleados_list.activated = True
        empleados_list.save()


    context = {
        'form': form,
        }

    return render(request,'proyecto/upload_batch_empleados.html', context)

def upload_batch_status(request):

    form = Status_BatchForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        form = Status_BatchForm()
        status_list = Status_Batch.objects.get(activated = False)
        f = open(status_list.file_name.path, 'r')
        reader = csv.reader(f)
        next(reader) #Advance past the reader

        for row in reader:
            ultimo_contrato = datetime.datetime.strptime(row[10], "%d/%m/%Y").date()
            planta = datetime.datetime.strptime(row[16], "%d/%m/%Y").date()
            planta_anterior = datetime.datetime.strptime(row[15], "%d/%m/%Y").date()
            if Perfil.objects.filter(numero_de_trabajador = row[0]):
                perfil = Perfil.objects.get(numero_de_trabajador = row[0])
                if Status.objects.filter(perfil__numero_de_trabajador = row[0]):
                    messages.error(request,f'El perfil del empleado #{row[0]} ya existe dentro de la base de datos')
                else:
                    if RegistroPatronal.objects.filter(patronal = row[1]):
                        registro_patronal = RegistroPatronal.objects.get(patronal = row[1])
                        if Nivel.objects.filter(nivel = row[8]):
                            nivel = Nivel.objects.get(nivel = row[8])
                            if Contrato.objects.filter(contrato = row[9]):
                                tipo_de_contrato = Contrato.objects.get(contrato = row[9])
                                if Sangre.objects.filter(sangre = row[11]):
                                    sangre = Sangre.objects.get(sangre = row[11])
                                    if Sexo.objects.filter(sexo = row[12]):
                                        genero = Sexo.objects.get(sexo = row[12])
                                        if Civil.objects.filter(estado_civil = row[14]):
                                            civil = Civil.objects.get(estado_civil = row[14])
                                            perfil.complete_status = True
                                            perfil.save()
                                            status = Status(perfil=perfil,registro_patronal= registro_patronal,nss=row[2],curp=row[3],rfc=row[4],telefono=row[5],profesion=row[6],
                                                    no_cedula=row[7],nivel=nivel,tipo_de_contrato=tipo_de_contrato,ultimo_contrato_vence=ultimo_contrato,tipo_sangre=sangre,sexo=genero,domicilio=row[13],
                                                    estado_civil=civil,fecha_planta_anterior=planta_anterior,fecha_planta=planta,complete=True,)

                                            status.save()
                                        else:
                                            messages.error(request,f'El estado civil no existe dentro de la base de datos, empleado #{row[0]}')
                                    else:
                                        messages.error(request,f'El genero no existe dentro de la base de datos, empleado #{row[0]}')
                                else:
                                    messages.error(request,f'El tipo de sangre no existe dentro de la base de datos, empleado #{row[0]}')
                            else:
                                messages.error(request,f'El tipo de contrato no existe dentro de la base de datos, empleado #{row[0]}')
                        else:
                            messages.error(request,f'El nivel no existe dentro de la base de datos, empleado #{row[0]}')

                    else:
                        messages.error(request,f'El registro patronal no existe dentro de la base de datos, empleado #{row[0]}')
            else:
                messages.error(request,f'El perfil del empleado #{row[0]} no existe dentro de la base de datos')
        status_list.activated = True
        status_list.save()



    context = {
        'form': form,
        }

    return render(request,'proyecto/upload_batch_status.html', context)

def upload_batch_costos(request):
    tablas= DatosISR.objects.all()
    quincena=Decimal(14.00)
    mes=Decimal(30.40)
    impuesto_est=Decimal(0.0315)
    sar=Decimal(0.02)
    cesantia=Decimal(0.04625)
    infonavit=Decimal(0.05)
    comision=Decimal(0.09)
    form = Costos_BatchForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        form = Costos_BatchForm()
        costo_list = Costos_Batch.objects.get(activated = False)
        f = open(costo_list.file_name.path, 'r')
        reader = csv.reader(f)
        next(reader) #Advance past the reader

        for row in reader:
            #planta = datetime.datetime.strptime(row[16], "%d/%m/%Y").date()
            #planta_anterior = datetime.datetime.strptime(row[15], "%d/%m/%Y").date()
            if Status.objects.filter(perfil__numero_de_trabajador = row[0]):
                status = Status.objects.get(perfil__numero_de_trabajador = row[0])
                if Costo.objects.filter(status__perfil__numero_de_trabajador = row[0]):
                    messages.error(request,f'El empleado #{row[0]} ya se encuentra en la base de datos')
                else:
                    if Puesto.objects.filter(puesto = row[1]):
                        puesto = Puesto.objects.get(puesto = row[1])

                        status.complete_costo = True

                        costo = Costo(status=status,puesto=puesto,neto_catorcenal_sin_deducciones=row[2],complemento_salario_catorcenal=row[3],sueldo_diario=row[4],sdi=row[5],
                                imms_obrero_patronal=row[6],amortizacion_infonavit=row[7],fonacot=row[8],apoyo_de_pasajes=row[9],apoyo_vist_familiar=row[10],estancia=row[11],renta=row[12],
                                campamento=row[13],apoyo_estudios=row[14],gasolina=row[15],amv=row[16],complete=True,)

                        neto_catorcenal_sin_deducciones = Decimal(row[2])
                        complemento_salario_catorcenal = Decimal(row[3])
                        sueldo_diario = Decimal(row[4])
                        sdi = Decimal(row[5])
                        imms_obrero_patronal = Decimal(row[6])
                        amortizacion_infonavit = Decimal(row[7])
                        fonacot = Decimal(row[8])
                        apoyo_de_pasajes = Decimal(row[9])
                        apoyo_vist_familiar = Decimal(row[10])
                        estancia = Decimal(row[11])
                        renta = Decimal(row[12])
                        campamento= Decimal(row[13])
                        apoyo_estudios= Decimal(row[14])
                        gasolina= Decimal(row[15])
                        amv= Decimal(row[16])

                        costo.total_deduccion = amortizacion_infonavit + fonacot
                        costo.neto_pagar = neto_catorcenal_sin_deducciones - costo.total_deduccion
                        costo.sueldo_mensual_neto = (neto_catorcenal_sin_deducciones/quincena)*mes
                        costo.complemento_salario_mensual = (complemento_salario_catorcenal/quincena)*mes
                        costo.sueldo_mensual = sueldo_diario*mes
                        costo.sueldo_mensual_sdi = sdi*mes
                        costo.total_percepciones_mensual = apoyo_de_pasajes + costo.sueldo_mensual
                        for tabla in tablas:
                            if costo.total_percepciones_mensual >= tabla.liminf:
                                costo.lim_inferior = tabla.liminf
                                costo.tasa=tabla.excedente
                                costo.cuota_fija=tabla.cuota
                            if costo.lim_inferior >= tabla.p_ingresos:
                                costo.subsidio=tabla.subsidio
                            costo.impuesto_estatal= costo.total_percepciones_mensual*impuesto_est
                            costo.sar= costo.sueldo_mensual_sdi*sar
                            costo.cesantia= costo.sueldo_mensual_sdi*cesantia
                            costo.infonavit= costo.sueldo_mensual_sdi*infonavit
                            costo.excedente= costo.total_percepciones_mensual - costo.lim_inferior
                            costo.impuesto_marginal= costo.excedente * costo.tasa
                            costo.impuesto= costo.impuesto_marginal + costo.cuota_fija
                            costo.isr= costo.impuesto
                            #dato.otros_bonos= dato.bonos.bonos_ct_ocho + dato.bonos.bonos_ct_nueve
                            costo.total_apoyosbonos_empleadocomp= apoyo_vist_familiar + estancia + renta + apoyo_estudios + amv + campamento + gasolina

                            costo.total_apoyosbonos_agregcomis = campamento #Modificar falta suma
                            costo.comision_complemeto_salario_bonos= (costo.complemento_salario_mensual + campamento)*comision #Falta suma dentro de la multiplicacion
                            costo.total_costo_empresa = costo.sueldo_mensual_neto + costo.complemento_salario_mensual + apoyo_de_pasajes + costo.impuesto_estatal + imms_obrero_patronal + costo.sar + costo.cesantia + costo.infonavit + costo.isr + costo.total_apoyosbonos_empleadocomp #+ costo.total_apoyosbonos_agregcomis + costo.comision_complemeto_salario_bonos
                            costo.ingreso_mensual_neto_empleado= costo.sueldo_mensual_neto + costo.complemento_salario_mensual + apoyo_de_pasajes + costo.total_apoyosbonos_empleadocomp # + costo.total_apoyosbonos_agregcomis


                        costo.save()
                    else:
                        messages.error(request,f'El puesto no existe dentro de la base de datos, empleado #{row[0]}')
            else:
                messages.error(request,f'El status del empleado #{row[0]} no existe dentro de la base de datos')

        costo_list.activated = True
        costo_list.save()
        status.save()


    context = {
        'form': form,
        }

    return render(request,'proyecto/upload_batch_costos.html', context)

def upload_batch_bancarios(request):

    form = Bancarios_BatchForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        form = Bancarios_BatchForm()
        bancarios_list = Bancarios_Batch.objects.get(activated = False)
        f = open(bancarios_list.file_name.path, 'r')
        reader = csv.reader(f)
        next(reader) #Advance past the reader

        for row in reader:
            if Status.objects.filter(perfil__numero_de_trabajador = row[0]):
                status = Status.objects.get(perfil__numero_de_trabajador = row[0])
                if DatosBancarios.objects.filter(status__perfil__numero_de_trabajador=row[0]):
                    messages.error(request,f'El empleado #{row[0]} ya existe dentro de la base de datos')
                else:
                    if Banco.objects.filter(banco = row[4]):
                        banco = Banco.objects.get(banco = row[4])
                        status.complete_bancarios = True
                        bancarios = DatosBancarios(status=status, no_de_cuenta=row[1], numero_de_tarjeta=row[2], clabe_interbancaria=row[3],banco=banco,complete=True,)
                        bancarios.save()
                    else:
                        messages.error(request,f'El banco no existe dentro de la base de datos, empleado #{row[0]}')
            else:
                messages.error(request,f'El empleado no existe dentro de la base de datos, empleado #{row[0]}')
        bancarios_list.activated = True
        bancarios_list.save()
        status.save()

    context = {
        'form': form,
        }

    return render(request,'proyecto/upload_batch_bancarios.html', context)

def reporte_pdf_uniformes(uniformes, pk):
    orden = Uniformes.objects.get(id=pk)
    uniformes = Uniforme.objects.filter(orden__id=pk)
    ropas = uniformes.aggregate(Sum('cantidad'))
    suma_ropas = ropas['cantidad__sum']
    cantidad = str(suma_ropas)
    #Configuration of the PDF object
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter)

    #Colores utilizados
    azul = Color(0.16015625,0.5,0.72265625)
    rojo = Color(0.59375, 0.05859375, 0.05859375)
    #Encabezado
    c.setFillColor(black)
    c.setLineWidth(.2)
    c.setFont('Helvetica',10)
    c.drawString(440,735,'Folio:')

    c.setFillColor(azul)
    c.setStrokeColor(azul)
    c.setLineWidth(20)
    c.line(20,760,585,760) #Linea azul superior
    c.setLineWidth(0.2)
    c.line(20,727.5,585,727.5) #Linea posterior horizontal
    c.line(250,727.5,250,590) #Linea vertical

    c.setFillColor(white)
    c.setLineWidth(.2)
    c.setFont('Helvetica',10)
    c.drawCentredString(295,755,'ORDEN DE UNIFORMES')

    c.drawInlineImage('static/images/Logo-Vordtec.png',50,620, 6 * cm, 3 * cm) #Imagen VORDCAB
    #Primera columna
    c.setFillColor(black)
    c.setFont('Helvetica',10)
    c.drawString(260,710,'Empleado #:')
    numero_trabajador = str(orden.status.perfil.numero_de_trabajador)
    c.drawString(325,710, numero_trabajador)
    c.drawString(260,690,'Nombre:',)
    c.drawString(325,690, orden.status.perfil.nombres)
    c.drawString(390,690, orden.status.perfil.apellidos)
    c.drawString(260,670,'Empresa:')
    empresa = str(orden.status.perfil.empresa)
    c.drawString(325,670, empresa)
    c.drawString(260,650,'Distrito')
    distrito = str(orden.status.perfil.distrito)
    c.drawString(325,650, distrito)
    c.drawString(260,630,'Fecha de pedido:')
    fecha = str(orden.fecha_pedido)
    c.drawString(345,630, fecha)
    c.drawString(260,610,'Cantidad total de piezas')
    c.drawString(380,610, cantidad)
    #Segunda columna
    #c.drawString(420,710,'Activo:')
    #c.drawString(420,690, 'NA')
    #c.drawString(420,670, 'Sector:')
    #c.drawString(420,650, 'NA')
    #c.drawString(420,630, 'Fecha Emisión:')
    #c.drawString(420,610,'28-06-2022 11:16:21')
    c.setFillColor(rojo) ## NUMERO DEL FOLIO
    id = str(orden.id)
    c.drawString(475,735, id)

    #Tabla y altura guia
    data =[]
    high = 550
    data.append(['''Orden #''','''Producto''','''Cantidad''', '''Talla''',])
    for uniforme in uniformes: #Salen todos los datos
        data.append([uniforme.id,uniforme.ropa,uniforme.cantidad,uniforme.talla,])
        high = high - 18

    #Observaciones
    c.setFillColor(azul)
    c.setLineWidth(20)
    c.line(20,high-35,585,high-35) #Linea posterior horizontal
    c.setFillColor(white)
    c.setLineWidth(.1)
    c.setFont('Helvetica-Bold',10)
    c.drawCentredString(295,high-40,'Observaciones')
    c.setFillColor(black)
    c.setFont('Helvetica',8)
    c.drawCentredString(295,high-60,'                                                                                                                ')
    c.drawCentredString(295,high-70,'                                                                                                                ')

    #Autorizacion parte
    c.setFillColor(azul)
    c.setFont('Helvetica',8)
    c.setLineWidth(1)
    c.line(150,high-150,275,high-150) #Linea posterior horizontal
    c.line(350,high-150,475,high-150) #Linea posterior horizontal
    c.setFillColor(black)
    c.drawCentredString(212.5,high-160,'Empleado')
    c.drawCentredString(412.5,high-160,'Aprobación')
    c.drawCentredString(180,high-145,orden.status.perfil.nombres)
    c.drawCentredString(240,high-145,orden.status.perfil.apellidos)

    c.drawCentredString(412.5,high-145,'Nombre aprobador')

    #Pie de pagina
    c.setFillColor(azul)
    c.setLineWidth(40)
    c.line(20,50,585,50) #Linea posterior horizontal
    c.setFillColor(white)
    #c.drawCentredString(70,53,'Clasificación:')
    #c.drawCentredString(140,53,'Nivel:')
    #c.drawCentredString(240,53,'Preparado por:')
    #c.drawCentredString(350,53,'Aprobado:')
    #c.drawCentredString(450,53,'Fecha emisión:')
    #c.drawCentredString(550,53,'Rev:')
    #Parte de abajo
    #c.drawCentredString(70,39,'Controlado')
    #c.drawCentredString(140,39,'N5')
    #c.drawCentredString(240,39,'SEOV-ALM-N4-01-01')
    #c.drawCentredString(350,39,'SUB ADM')
    #c.drawCentredString(450,39,'24/Oct/2018')
    #c.drawCentredString(550,39,'001')

    #Propiedades de la tabla
    width, height = letter
    table = Table(data, colWidths=[2.6 * cm, 2.6 * cm, 11.8 * cm, 2.6 * cm], repeatRows=1)
    table.setStyle(TableStyle([ #estilos de la tabla
        #ENCABEZADO
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TEXTCOLOR',(0,0),(-1,0), white),
        ('FONTSIZE',(0,0),(-1,0), 13),
        ('BACKGROUND',(0,0),(-1,0), azul),
        #CUERPO
        ('TEXTCOLOR',(0,1),(-1,-1), colors.black),
        ('FONTSIZE',(0,1),(-1,-1), 10),
        ]))
    table.wrapOn(c, width, height)
    table.drawOn(c, 25, high)
    c.save()
    c.showPage()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='pruebauniforme.pdf')

def reporte_pdf_costo_detalles(costo):
    now = datetime.date.today()
    fecha = str(now)
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter)

    #Colores utilizados
    azul = Color(0.16015625,0.5,0.72265625)
    rojo = Color(0.59375, 0.05859375, 0.05859375)
    #Encabezado
    c.setFillColor(black)
    c.setLineWidth(.2)
    c.setFont('Helvetica',10)
    c.drawString(240,735,'Fecha del costo:')
    created_at = str(costo.created_at)
    c.drawString(330,735,created_at)
    c.drawString(440,735,'Fecha reporte:')
    c.drawString(510,735,fecha)

    c.setFillColor(azul)
    c.setStrokeColor(azul)
    c.setLineWidth(20)
    c.line(20,760,585,760) #Linea azul superior
    c.setLineWidth(0.2)
    c.line(20,727.5,585,727.5) #Linea posterior horizontal
    c.line(250,727.5,250,590) #Linea vertical

    c.setFillColor(white)
    c.setLineWidth(.2)
    c.setFont('Helvetica',10)
    c.drawCentredString(295,755,'Detalles de Costo')

    #c.drawInlineImage(costo.status.perfil.empresa.logo,50,620, 6 * cm, 3 * cm) #Imagen VORDCAB
    logo = ImageReader(costo.status.perfil.empresa.logo)
    c.drawImage(logo,70,640, 4 * cm, 2 * cm)
    #Primera columna
    c.setFillColor(black)
    c.setFont('Helvetica-Bold',10)
    c.drawString(260,710,'Empleado #:')
    c.drawString(260,690,'Nombre:',)
    c.drawString(260,670,'Empresa:')
    c.drawString(260,650,'Distrito')
    c.line(20,590,585,590) #Linea posterior horizontal
    #Primera columna
    c.drawString(40,575,'Puesto:')
    c.drawString(40,550,'Amortización infonavit:')
    c.drawString(40,525,'Fonacot:')
    c.drawString(40,500,'Neto catorcenal sin deducciones:')
    c.drawString(40,475,'Complemento salario catorcenal:')
    c.drawString(40,450,'Sueldo diario:')
    c.drawString(40,425,'SDI:')
    c.drawString(40,400,'Apoyo de pasajes:')
    c.drawString(40,375,'IMSS obrero patronal:')
    c.drawString(40,350,'Apoyo visita familiar:')
    c.drawString(40,325,'Estancia:')
    c.drawString(40,300,'Renta:')
    c.drawString(40,275,'Apoyo de estudios:')
    c.drawString(40,250,'Apoyo mantenimiento vehicular:')
    c.drawString(40,225,'Gasolina:')
    c.drawString(40,200,'Campamento:')
    c.drawString(40,175,'Total deducción:')
    c.drawString(40,150,'Neto a pagar:')
    c.drawString(40,125,'Sueldo mensual neto:')
    #Segunda columna
    c.drawString(300,575,'Sueldo mensual:')
    c.drawString(300,550,'Sueldo mensual SDI:')
    c.drawString(300,525,'Total percepcion mensual:')
    c.drawString(300,500,'Impuesto estatal:')
    c.drawString(300,475,'SAR:')
    c.drawString(300,450,'Cesantia:')
    c.drawString(300,425,'Infonavit:')
    c.drawString(300,400,'ISR:')
    c.drawString(300,375,'Limite inferior:')
    c.drawString(300,350,'Excedente:')
    c.drawString(300,325,'Tasa:')
    c.drawString(300,300,'Impuesto marginal:')
    c.drawString(300,275,'Cuota fija:')
    c.drawString(300,250,'Impuesto:')
    c.drawString(300,225,'Subsidio:')
    c.drawString(300,200,'Total apoyos y bonos empleado comprueba:')
    c.drawString(300,175,'Bono total:')
    c.drawString(300,150,'Comision complemento de salario bonos:')
    c.drawString(300,125,'Total costo para la empresa:')
    c.drawString(300,100,'Ingreso mensual neto del empleado:')
    c.setFont('Helvetica',10)
    #Parte superior
    numero_trabajador = str(costo.status.perfil.numero_de_trabajador)
    c.drawString(325,710, numero_trabajador)
    c.drawString(325,690, costo.status.perfil.nombres)
    c.drawString(390,690, costo.status.perfil.apellidos)
    empresa = str(costo.status.perfil.empresa)
    c.drawString(325,670, empresa)
    distrito = str(costo.status.perfil.distrito)
    c.drawString(325,650, distrito)
    #Primera columna
    puesto = str(costo.puesto)
    c.drawString(90,575,puesto)
    c.drawString(170,550,costo.amortizacion_infonavit)
    c.drawString(100,525,costo.fonacot)
    c.drawString(220,500,costo.neto_catorcenal_sin_deducciones)
    c.drawString(220,475,costo.complemento_salario_catorcenal)
    c.drawString(130,450,costo.sueldo_diario)
    c.drawString(80,425,costo.sdi)
    c.drawString(150,400,costo.apoyo_de_pasajes)
    c.drawString(170,375,costo.imms_obrero_patronal)
    c.drawString(170,350,costo.apoyo_vist_familiar)
    c.drawString(100,325,costo.estancia)
    c.drawString(100,300,costo.impuesto_marginal)
    c.drawString(150,275,costo.apoyo_estudios)
    c.drawString(220,250,costo.amv)
    c.drawString(120,225,costo.gasolina)
    c.drawString(130,200,costo.campamento)
    c.drawString(140,175,costo.total_deduccion)
    c.drawString(120,150,costo.neto_pagar)
    c.drawString(170,125,costo.sueldo_mensual_neto)
    #Segunda columna
    c.drawString(405,575,costo.sueldo_mensual)
    c.drawString(425,550,costo.sueldo_mensual_sdi)
    c.drawString(445,525,costo.total_percepciones_mensual)
    c.drawString(405,500,costo.impuesto_estatal)
    c.drawString(365,475,costo.sar)
    c.drawString(365,450,costo.cesantia)
    c.drawString(365,425,costo.infonavit)
    c.drawString(365,400,costo.isr)
    c.drawString(395,375,costo.lim_inferior)
    c.drawString(385,350,costo.excedente)
    c.drawString(355,325,costo.tasa)
    c.drawString(415,300,costo.impuesto_marginal)
    c.drawString(365,275,costo.cuota_fija)
    c.drawString(365,250,costo.impuesto)
    c.drawString(365,225,costo.subsidio)
    c.drawString(525,200,costo.total_apoyosbonos_empleadocomp)
    c.drawString(375,175,costo.bonototal)
    c.drawString(515,150,costo.comision_complemeto_salario_bonos)
    c.drawString(465,125,costo.total_costo_empresa)
    c.drawString(485,100,costo.ingreso_mensual_neto_empleado)

    #Pie de pagina
    c.setFillColor(azul)
    c.setLineWidth(40)
    c.line(20,50,585,50) #Linea posterior horizontal
    c.setFillColor(white)
    #c.drawCentredString(70,53,'Clasificación:')
    #c.drawCentredString(140,53,'Nivel:')
    #c.drawCentredString(240,53,'Preparado por:')
    #c.drawCentredString(350,53,'Aprobado:')
    #c.drawCentredString(450,53,'Fecha emisión:')
    #c.drawCentredString(550,53,'Rev:')
    #Parte de abajo
    #c.drawCentredString(70,39,'Controlado')
    #c.drawCentredString(140,39,'N5')
    #c.drawCentredString(240,39,'SEOV-ALM-N4-01-01')
    #c.drawCentredString(350,39,'SUB ADM')
    #c.drawCentredString(450,39,'24/Oct/2018')
    #c.drawCentredString(550,39,'001')
    c.save()
    c.showPage()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='CostoDetalle.pdf')

def reporte_pdf_economico_detalles(economicos,empleado):
    now = datetime.date.today()
    fecha = str(now)
    #Colores utilizados
    azul = Color(0.16015625,0.5,0.72265625)
    rojo = Color(0.59375, 0.05859375, 0.05859375)
    if empleado.complete_dias == True:
        estado = "Complete"
        color = azul
    else:
        estado = "Incomplete"
        color = rojo
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter)

    #Encabezado
    c.setFillColor(black)
    c.setLineWidth(.2)
    c.setFont('Helvetica',10)
    c.drawString(440,735,'Fecha reporte:')
    c.drawString(510,735,fecha)

    c.setFillColor(azul)
    c.setStrokeColor(azul)
    c.setLineWidth(20)
    c.line(20,760,585,760) #Linea azul superior
    c.setLineWidth(0.2)
    c.line(20,727.5,585,727.5) #Linea posterior horizontal
    c.line(250,727.5,250,590) #Linea vertical

    c.setFillColor(white)
    c.setLineWidth(.2)
    c.setFont('Helvetica',10)
    c.drawCentredString(295,755,'Detalle de días economicos')

    #c.drawInlineImage(costo.status.perfil.empresa.logo,50,620, 6 * cm, 3 * cm) #Imagen VORDCAB
    logo = ImageReader(empleado.status.perfil.empresa.logo)
    c.drawImage(logo,70,640, 4 * cm, 2 * cm)
    #Primera columna
    c.setFillColor(black)
    c.setFont('Helvetica-Bold',10)
    c.drawString(260,710,'Empleado #:')
    c.drawString(260,690,'Nombre:',)
    c.drawString(260,670,'Empresa:')
    c.drawString(260,650,'Distrito:')
    c.drawString(260,630,'Estado:')
    c.line(20,590,585,590) #Linea posterior horizontal

    c.setFont('Helvetica',10)
    #Parte superior
    numero_trabajador = str(empleado.status.perfil.numero_de_trabajador)
    c.drawString(325,710, numero_trabajador)
    c.drawString(325,690, empleado.status.perfil.nombres)
    c.drawString(390,690, empleado.status.perfil.apellidos)
    empresa = str(empleado.status.perfil.empresa)
    c.drawString(325,670, empresa)
    distrito = str(empleado.status.perfil.distrito)
    c.drawString(325,650, distrito)
    c.setFillColor(color)
    c.drawString(325,630, estado)
    c.setFillColor(black)
    #Tabla y altura guia
    data =[]
    high = 570
    data.append(['''Periodo''','''Fecha''','''Días disfrutados''', '''Días pendientes''','''Creado''',])
    for economico in economicos: #Salen todos los datos
        creado = economico.created_at.date()
        data.append([economico.periodo,economico.fecha,economico.dias_disfrutados,economico.dias_pendientes,creado,])
        high = high - 18

    #Pie de pagina
    c.setFillColor(azul)
    c.setLineWidth(40)
    c.line(20,50,585,50) #Linea posterior horizontal
    c.setFillColor(white)
    #c.drawCentredString(70,53,'Clasificación:')
    #c.drawCentredString(140,53,'Nivel:')
    #c.drawCentredString(240,53,'Preparado por:')
    #c.drawCentredString(350,53,'Aprobado:')
    #c.drawCentredString(450,53,'Fecha emisión:')
    #c.drawCentredString(550,53,'Rev:')
    #Parte de abajo
    #c.drawCentredString(70,39,'Controlado')
    #c.drawCentredString(140,39,'N5')
    #c.drawCentredString(240,39,'SEOV-ALM-N4-01-01')
    #c.drawCentredString(350,39,'SUB ADM')
    #c.drawCentredString(450,39,'24/Oct/2018')
    #c.drawCentredString(550,39,'001')
        #Propiedades de la tabla
    width, height = letter
    table = Table(data, colWidths=[3.2 * cm, 3.2 * cm, 4.2 * cm, 4.5 * cm, 4.5 * cm], repeatRows=1)
    table.setStyle(TableStyle([ #estilos de la tabla
        #ENCABEZADO
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TEXTCOLOR',(0,0),(-1,0), white),
        ('FONTSIZE',(0,0),(-1,0), 13),
        ('BACKGROUND',(0,0),(-1,0), azul),
        #CUERPO
        ('TEXTCOLOR',(0,1),(-1,-1), colors.black),
        ('FONTSIZE',(0,1),(-1,-1), 10),
        ]))
    table.wrapOn(c, width, height)
    table.drawOn(c, 25, high)
    c.save()
    c.showPage()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='EconomicoDetalle.pdf')