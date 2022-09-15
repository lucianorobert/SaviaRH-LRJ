from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords



 #Tabla de vacaciones
class TablaVacaciones(models.Model):
    years = models.IntegerField(null=True)
    days = models.IntegerField(null=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return f'Años: {self.years}, dias de vacaciones: {self.days}'

class Empresa(models.Model):
    empresa = models.CharField(max_length=50,null=True)
    complete = models.BooleanField(default=False)
    logo = models.ImageField(blank=True, upload_to="logo/")

    @property
    def logoURL(self):
        try:
            url = self.logo.url
        except:
            url = ''
        return url


    def __str__(self):
        return f'{self.empresa}'

class Puesto(models.Model):
    puesto = models.CharField(max_length=50,null=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.puesto}'

class Distrito(models.Model):
    distrito = models.CharField(max_length=50,null=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.distrito}'
class Proyecto(models.Model):
    proyecto = models.CharField(max_length=50,null=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.proyecto}'
class SubProyecto(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete = models.CASCADE, null=True)
    subproyecto = models.CharField(max_length=50,null=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.subproyecto}'
class Contrato(models.Model):
    contrato = models.CharField(max_length=50,null=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.contrato}'
class Sangre(models.Model):
    sangre = models.CharField(max_length=50,null=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.sangre}'
class Sexo(models.Model):
    sexo = models.CharField(max_length=50,null=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.sexo}'
class Civil(models.Model):
    estado_civil = models.CharField(max_length=50,null=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.estado_civil}'
class Banco(models.Model):
    banco = models.CharField(max_length=50,null=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.banco}'

class RegistroPatronal(models.Model):
    patronal = models.CharField(max_length=50,null=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.patronal}'




    #Tabla ISR
class DatosISR(models.Model):
    liminf = models.DecimalField(max_digits=14, decimal_places=2,null=True)
    limsup = models.DecimalField(max_digits=14, decimal_places=2,null=True)
    cuota = models.DecimalField(max_digits=14, decimal_places=2,null=True)
    excedente = models.DecimalField(max_digits=14, decimal_places=4,null=True)
    p_ingresos = models.DecimalField(max_digits=14, decimal_places=2,null=True)
    g_ingresos = models.DecimalField(max_digits=14, decimal_places=2,null=True)
    subsidio = models.DecimalField(max_digits=14, decimal_places=2,null=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        if self.complete == False:
            return "Campo vacio"
        return f'{self.liminf} - {self.limsup} - {self.cuota} - {self.excedente} - {self.p_ingresos} - {self.g_ingresos} - {self.subsidio}'

class UserDatos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    distrito = models.ForeignKey(Distrito, on_delete = models.CASCADE, null=True)
    def __str__(self):
        return f'{self.user}, distrito: {self.distrito} '

class Perfil(models.Model):
    foto = models.ImageField(null=True, blank=True, upload_to="perfil/")
    numero_de_trabajador = models.IntegerField(null=True)
    empresa = models.ForeignKey(Empresa, on_delete = models.CASCADE, null=True)
    distrito = models.ForeignKey(Distrito, on_delete = models.CASCADE, null=True)
    nombres = models.CharField(max_length=50,null=True)
    apellidos = models.CharField(max_length=50,null=True)
    fecha_nacimiento = models.DateField(null=True)
    correo_electronico = models.EmailField(max_length=50)
    proyecto = models.ForeignKey(Proyecto, on_delete = models.CASCADE, null=True)
    subproyecto = models.ForeignKey(SubProyecto, on_delete = models.CASCADE, null=True)
    complete = models.BooleanField(default=False)
    complete_status = models.BooleanField(default=False)


    @property
    def fotoURL(self):
        try:
            url = self.foto.url
        except:
            url = ''
        return url


    def __str__(self):
        if self.complete == False:
            return "Campo vacio"
        return f'{self.nombres} {self.apellidos}' or ''

 #Tabla de vacaciones
class Nivel(models.Model):
    nivel = models.IntegerField(null=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.nivel}'

class Status(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete = models.CASCADE, null=True)
    registro_patronal = models.ForeignKey(RegistroPatronal, on_delete = models.CASCADE, null=True)
    nss = models.CharField(max_length=50,null=True)
    curp = models.CharField(max_length=50,null=True)
    rfc = models.CharField(max_length=50,null=True)
    telefono = models.CharField(max_length=50,null=True,blank=True, default='NR')
    profesion = models.CharField(max_length=50,null=True)
    no_cedula = models.CharField(max_length=50,null=True)
    nivel = models.ForeignKey(Nivel, on_delete = models.CASCADE, null=True)
    tipo_de_contrato = models.ForeignKey(Contrato, on_delete = models.CASCADE, null=True)
    ultimo_contrato_vence = models.DateField(null=True)
    tipo_sangre = models.ForeignKey(Sangre, on_delete = models.CASCADE, null=True)
    sexo = models.ForeignKey(Sexo, on_delete = models.CASCADE, null=True)
    domicilio = models.CharField(max_length=60,null=True)
    estado_civil = models.ForeignKey(Civil, on_delete = models.CASCADE, null=True)
    fecha_planta_anterior = models.DateField(null=True, blank=True)
    fecha_planta = models.DateField(null=True)
    complete = models.BooleanField(default=False)
    complete_costo = models.BooleanField(default=False)
    complete_bancarios = models.BooleanField(default=False)
    complete_vacaciones = models.BooleanField(default=False)
    complete_uniformes = models.BooleanField(default=False)
    complete_economicos = models.BooleanField(default=False)
    def __str__(self):
        if self.perfil ==None:
            return "Campo vacio"
        return f'{self.perfil.nombres} {self.perfil.apellidos}' or ''

class DatosBancarios(models.Model):
    status = models.ForeignKey(Status, on_delete = models.CASCADE, null=True)
    no_de_cuenta = models.CharField(max_length=50,null=True)
    numero_de_tarjeta = models.CharField(max_length=50,null=True)
    clabe_interbancaria = models.CharField(max_length=50,null=True)
    banco = models.ForeignKey(Banco, on_delete = models.CASCADE, null=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        if self.status ==None:
            return "Campo vacio"
        return f'{self.status.perfil.nombres} {self.status.perfil.apellidos}'




class Costo(models.Model):
    #Independientes (formulario)
    status = models.ForeignKey(Status, on_delete = models.CASCADE, null=True)
    seccion = models.CharField(max_length=50,null=True)
    puesto = models.ForeignKey(Puesto, on_delete = models.CASCADE, null=True)
    amortizacion_infonavit = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    fonacot = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    neto_catorcenal_sin_deducciones = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    complemento_salario_catorcenal = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    sueldo_diario = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    sdi = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    apoyo_de_pasajes = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    imms_obrero_patronal = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    apoyo_vist_familiar = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    estancia = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    renta = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    apoyo_estudios = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    amv = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    gasolina = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    campamento = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    #Dependientes
    total_deduccion = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    neto_pagar = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    sueldo_mensual_neto = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    complemento_salario_mensual = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    sueldo_mensual = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    sueldo_mensual_sdi = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    total_percepciones_mensual = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    impuesto_estatal = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    sar = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    cesantia = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    infonavit = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    isr = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    lim_inferior = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    excedente = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    tasa = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    impuesto_marginal = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    cuota_fija = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    impuesto = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    subsidio = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    total_apoyosbonos_empleadocomp = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    #Variables
    total_apoyosbonos_agregcomis = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    comision_complemeto_salario_bonos = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    total_costo_empresa = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    ingreso_mensual_neto_empleado = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    #Otros
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    complete = models.BooleanField(default=False)
    history = HistoricalRecords(history_change_reason_field=models.TextField(null=True))
    def __str__(self):
        if self.status ==None:
            return "Campo vacio"
        return f'{self.status.perfil.nombres} {self.status.perfil.apellidos}'

class Bonos(models.Model):
    costo = models.ForeignKey(Costo, on_delete = models.CASCADE, null=True)
    datosbancarios = models.ForeignKey(DatosBancarios, on_delete = models.CASCADE, null=True)
    monto = models.DecimalField(max_digits=14, decimal_places=2,null=True, default=0)
    fecha_bono = models.DateField(null=True)
    mes_bono = models.DateField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)
    history = HistoricalRecords(history_change_reason_field=models.TextField(null=True))
    def __str__(self):
        if self.costo ==None:
            return "Campo vacio"
        return f'{self.costo.status.perfil.nombres} {self.costo.status.perfil.apellidos} {self.fecha_bono}'

class Catorcenas(models.Model):
    catorcena = models.IntegerField(null=True, default=0)
    fecha_inicial = models.DateField(null=True)
    fecha_final = models.DateField(null=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return f' bono: {self.catorcena}, inicia {self.fecha_inicial} finaliza: {self.fecha_final}'
    class Meta:
        unique_together = ('catorcena', 'fecha_inicial',)

class Ropa(models.Model):
    ropa = models.CharField(max_length=50,null=True)
    complete = models.BooleanField(default=False)
    seleccionado = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.ropa}'

class Tallas(models.Model):
    ropa = models.ForeignKey(Ropa, on_delete = models.CASCADE, null=True)
    talla = models.CharField(max_length=50,null=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return f'Ropa: {self.ropa}, Talla: {self.talla}'

class Uniformes(models.Model):
    status = models.ForeignKey(Status, on_delete = models.CASCADE, null=True)
    fecha_pedido = models.DateField(null=True)
    #uniformes_totales = models.IntegerField(null=True, default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)
    history = HistoricalRecords(history_change_reason_field=models.TextField(null=True))
    def __str__(self):
        if self.status == None:
            return "Campo vacio"
        return f'{self.status.perfil.nombres} {self.status.perfil.apellidos}'

class Uniforme(models.Model):
    orden = models.ForeignKey(Uniformes, on_delete = models.CASCADE, null=True)
    talla = models.ForeignKey(Tallas, on_delete = models.CASCADE, null=True)
    ropa = models.ForeignKey(Ropa, on_delete = models.CASCADE, null=True)
    fecha_entrega = models.DateField(null=True)
    cantidad = models.IntegerField(null=True, default=0)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return f'Ropa: {self.ropa} Talla: {self.talla} Cantidad: {self.cantidad}'


class Vacaciones(models.Model):
    status = models.ForeignKey(Status, on_delete = models.CASCADE, null=True)
    periodo = models.CharField(max_length=50,null=True)
    dias_de_vacaciones = models.IntegerField(null=True, default=0)
    dias_disfrutados = models.IntegerField(null=True, default=0)
    total_pendiente = models.IntegerField(null=True, default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)
    history = HistoricalRecords(history_change_reason_field=models.TextField(null=True))
    def __str__(self):
        if self.status == None:
            return "Campo vacio"
        return f'{self.status.perfil.nombres} {self.status.perfil.apellidos}'


class Economicos(models.Model):
    status = models.ForeignKey(Status, on_delete = models.CASCADE, null=True)
    periodo = models.CharField(max_length=50,null=True)
    dias_pendientes = models.IntegerField(null=True, default=0)
    dias_disfrutados = models.IntegerField(null=True, default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)
    history = HistoricalRecords(history_change_reason_field=models.TextField(null=True))
    def __str__(self):
        if self.status == None:
            return "Campo vacio"
        return f'{self.status.perfil.nombres} {self.status.perfil.apellidos}'

class Empleados_Batch(models.Model):
    file_name = models.FileField(upload_to='product_bash')
    uploaded = models.DateField(auto_now_add=True)
    activated = models.BooleanField(default=False)


    def __str__(self):
        return f'File id:{self.id}'

class Status_Batch(models.Model):
    file_name = models.FileField(upload_to='product_bash')
    uploaded = models.DateField(auto_now_add=True)
    activated = models.BooleanField(default=False)


    def __str__(self):
        return f'File id:{self.id}'



