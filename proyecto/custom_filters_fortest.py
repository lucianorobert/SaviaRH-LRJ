from django import template

register = template.Library()

day_names = {
    '1': 'Lunes',
    '2': 'Martes',
    '3': 'Miercoles',
    '4': 'Jueves',
    '5': 'Viernes',
    '6': 'Sabado',
    '7': 'Domingo',
}

@register.filter
def get_day_name(value):
    return day_names.get(value, '')


# models.py

# class Solicitud_vacaciones(models.Model):
#     status = models.ForeignKey(Status, on_delete = models.CASCADE, null=True)
#     fecha_inicio = models.DateField(null=True)
#     fecha_fin = models.DateField(null=True)
#     dia_inhabil = models.ForeignKey(Dia_vacacion, on_delete = models.CASCADE, blank=True, null=True)
#     autorizar = models.BooleanField(null=True, default=None)
#     razon_no_autorizado = models.TextField(null=True)

#     def __str__(self):
#         return f' id: {self.id} Status: {self.status} Fecha solicitud: {self.created_at} Días: {self.fecha_inicio} a {self.fecha_fin}'
    
# # views.py
# @login_required(login_url='user-login')
# def solicitud_vacacion_verificar(request, pk):
#     solicitud = Solicitud_vacaciones.objects.get(id=pk)

#     if request.method == 'POST' and 'btnSend' in request.POST:
#         if solicitud.fecha_fin < solicitud.fecha_inicio:
#             messages.error(request,'La fecha de inicio no puede ser posterior a la final')
#             valido=False

#         inhabil = solicitud.dia_inhabil.numero
#         # inhabil = solicitud.dia_inhabil
        
#         for fecha in (solicitud.fecha_inicio + timedelta(n) for n in range(day_count)):
#             if fecha.isoweekday() == inhabil:
#                 cuenta -= 1
#             else:
#                 for dia in tabla_festivos:
#                     if fecha == dia.dia_festivo:
#                         cuenta -= 1  #Días que va a tomar con esta solicitud
#         dias_vacacion = cuenta
#         if cuenta < 0: 
#             messages.error(request, 'La cantidad de días que disfrutara debe ser mayor a 0')
#             valido=False    
        
    
#         solicitud.autorizar = True
#         solicitud.save()
#         messages.success(request, 'Solicitud autorizada y días de vacaciones agregados')
    
#         return redirect('Solicitudes_vacaciones')
#     elif 'btnSave':
#         solicitud.razon_no_autorizado = request.POST.get('reason')
#         solicitud.autorizar = False
#         solicitud.save()
#         messages.error(request, 'Solicitud autorizada y días de vacaciones agregados')
#         return redirect('Solicitudes_vacaciones')

#     else:
#         form = SolicitudVacacionesUpdateForm(instance=solicitud)

#     context = {'form':form,'solicitud':solicitud, 'temas':temas, 'trabajos':trabajos}

#     return render(request,'proyecto/solicitud_vacaciones_update.html',context)


# #template.html
# <!-- <!DOCTYPE html>
# <html>
# <body>
#     <div class="container">
#         <h1>Day of the Week Form</h1>
#         <form method="POST"">
#             {% csrf_token %}
            
#             <div class="form-group">
#                 <button type="submit" class="btn btn-primary btn-lg">Authorize</button>
#                 <button type="button" class="btn btn-danger btn-lg" data-toggle="modal" data-target="#notAuthorizeModal">Not Authorize</button>
#             </div>
#         </form>
#     </div>

#     <!-- Not Authorize Modal -->
#     <!-- <div class="modal fade" id="notAuthorizeModal" tabindex="-1" role="dialog" aria-labelledby="notAuthorizeModalLabel" aria-hidden="true">
#         <div class="modal-dialog" role="document">
#             <div class="modal-content">
#                 <div class="modal-header">
#                     <h5 class="modal-title" id="notAuthorizeModalLabel">Reason for Not Authorization</h5>
#                     <button type="button" class="close" data-dismiss="modal" aria-label="Close">
#                         <span aria-hidden="true">&times;</span>
#                     </button>
#                 </div>
#                 <div class="modal-body">
#                     <textarea class="form-control" name="reason" rows="4" placeholder="Enter reason for not authorizing"></textarea>
#                 </div>
#                 <div class="modal-footer">
#                     <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
#                     <button type="submit" class="btn btn-danger" name="btnSave">Submit</button>
#                 </div>
#             </div>
#         </div>
#     </div>
# </body>
# </html> -->

# I'd like to update in Solicitud_vacaciones model the fields razon_no_autorizado to what is in reason from notAuthorizeModal, and autorizar to False. Now i'm getting the error:
# IntegrityError at /proyecto/Solicitud_vacacion_autorizar/1/
# (1048, "Column 'razon_no_autorizado' cannot be null")
# Request Method:	GET
# Request URL:	http://localhost:8000/proyecto/Solicitud_vacacion_autorizar/1/
# Django Version:	4.0.4
# Exception Type:	IntegrityError
# Exception Value:	
# (1048, "Column 'razon_no_autorizado' cannot be null")
# Exception Location:	D:\Programming\SAVIARH-LRJ\myenv-saviarh\lib\site-packages\django\db\backends\mysql\base.py, line 80, in execute
# Python Executable:	D:\Programming\SAVIARH-LRJ\myenv-saviarh\Scripts\python.exe
# Python Version:	3.9.5