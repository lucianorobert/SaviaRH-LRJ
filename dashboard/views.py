#from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import FileResponse

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch,cm,mm
from reportlab.lib.pagesizes import letter,A4,landscape
import io
from reportlab.lib import colors
from reportlab.lib.colors import Color, black, blue, red, white
from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, NextPageTemplate, PageBreak, PageTemplate,Table, SimpleDocTemplate,TableStyle
from reportlab.lib.styles import getSampleStyleSheet
import os
from proyecto.models import Perfil
#from django.contrib.auth.decorators import login_required
#from .filters import ArticulosparaSurtirFilter
from django.http import HttpResponse
from openpyxl import Workbook
from openpyxl.styles import NamedStyle, Font, PatternFill
from openpyxl.utils import get_column_letter
import datetime
from django.db.models.functions import Concat, Extract
from django.db.models import Value
#PDF generator
from django.db.models import Q
from openpyxl.drawing.image import Image
from openpyxl.chart import PieChart, LineChart, Reference
from openpyxl.chart.axis import DateAxis
from collections import Counter
from proyecto.models import Costo, Bonos
from django.db.models import Sum
from django.core.mail import send_mail
from django.conf import settings
import locale
locale.setlocale( locale.LC_ALL, '' )


def index(request):

    perfiles = Perfil.objects.filter(complete = True)
    cantidad = perfiles.count()

    context = {
        'cantidad': cantidad,
    }

    return render(request, 'dashboard/inform_list.html', context)


def mensaje(request):
    if request.method == 'POST':
        subject=request.POST["asunto"]
        message=request.POST["mensaje"] + " " + request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["halo-victor45@hotmail.com"]
        send_mail(subject, message, email_from, recipient_list)

        return redirect('index')

    return render(request, 'dashboard/Mensaje.html')


def render_report(request,pk):
    costo_ver = Costo.objects.get(id = pk)
    costo = Costo.history.filter(~Q(sueldo_mensual_neto=None)|~Q(sueldo_mensual_neto=0), id=pk)
    bonos = (Bonos.objects.filter(costo=costo_ver).annotate(month=Extract('mes_bono','month')).values('month')
                        .annotate(total=Sum('monto')).order_by("month"))

    meses =  datetime.date.today().month

    meses_cost={}



    for mes in range(1,meses+1):
        cost = Costo.history.filter(~Q(sueldo_mensual_neto = None)|~Q(sueldo_mensual_neto = 0),id=pk, updated_at__month__gte= mes).first()
        if cost:
            meses_cost[mes] = cost.total_costo_empresa

    context = {
        'bonos':bonos,
        'registros':costo,
        'meses':meses,
        'meses_cost':meses_cost,
        }


    return render(request, 'dashboard/optional_report.html',context)