import django_filters
from django.db.models import Q
from .models import Perfil, Status, Bonos, Costo, DatosBancarios, Vacaciones, Uniformes, Economicos, Catorcenas, Distrito, Empresa
from .models import Solicitud_vacaciones, Solicitud_economicos
from django_filters import DateFilter, CharFilter

class PerfilFilter(django_filters.FilterSet):
    #nombres = django_filters.CharFilter(field_name='nombres', lookup_expr='icontains')
    nombres_apellidos = CharFilter(method ='my_filter', label="Search")

    class Meta:
        model = Perfil
        fields = ['numero_de_trabajador','empresa','distrito','nombres_apellidos','proyecto','subproyecto',]

    def my_filter(self, queryset, name, value):
        return queryset.filter(Q(nombres__icontains = value) | Q(apellidos__icontains = value))

class StatusFilter(django_filters.FilterSet):
    numero_de_trabajador = django_filters.NumberFilter(field_name='perfil__numero_de_trabajador')
    empresa = django_filters.CharFilter(field_name='perfil__empresa__empresa', lookup_expr='icontains')
    distrito = django_filters.ModelChoiceFilter(queryset=Distrito.objects.all(), field_name='perfil__distrito__distrito')
    nombres = CharFilter(method ='nombres_filter', label="Search")
    profesion = django_filters.CharFilter(field_name='profesion', lookup_expr='icontains')

    class Meta:
        model = Status
        fields = ['numero_de_trabajador','empresa','nombres','profesion','tipo_de_contrato','distrito']

    def nombres_filter(self, queryset, name, value):
        return queryset.filter(Q(perfil__nombres__icontains = value) | Q(perfil__apellidos__icontains = value))

class BancariosFilter(django_filters.FilterSet):
    nombres = CharFilter(method ='nombres_filter', label="Search")
    no_de_cuenta = django_filters.CharFilter(field_name='no_de_cuenta', lookup_expr='icontains')
    class Meta:
        model = DatosBancarios
        fields = ['nombres','no_de_cuenta','banco',]

    def nombres_filter(self, queryset, name, value):
        return queryset.filter(Q(status__perfil__nombres__icontains = value) | Q(status__perfil__apellidos__icontains = value))

class CostoFilter(django_filters.FilterSet):
    numero_de_trabajador = django_filters.NumberFilter(field_name='status__perfil__numero_de_trabajador')
    nombres = CharFilter(method ='nombres_filter', label="Search")
    empresa = django_filters.ModelChoiceFilter(queryset=Empresa.objects.all(), field_name='status__perfil__empresa_empresa')
    distrito = django_filters.ModelChoiceFilter(queryset=Distrito.objects.all(), field_name='status__perfil__distrito__distrito')
    #proyecto = django_filters.CharFilter(field_name='status__perfil__proyecto', lookup_expr='icontains')
    #subproyecto = django_filters.CharFilter(field_name='status__perfil__subproyecto', lookup_expr='icontains')

    class Meta:
        model = Costo
        fields = ['numero_de_trabajador','nombres','empresa','distrito']

    def nombres_filter(self, queryset, name, value):
        return queryset.filter(Q(status__perfil__nombres__icontains = value) | Q(status__perfil__apellidos__icontains = value))

class BonosFilter(django_filters.FilterSet):
    nombres = CharFilter(method ='nombres_filter', label="Search")
    start_date = DateFilter(field_name = 'fecha_bono', lookup_expr='gte')
    end_date = DateFilter(field_name = 'fecha_bono', lookup_expr='lte')

    class Meta:
        model = Bonos
        fields = ['start_date','end_date','nombres']

    def nombres_filter(self, queryset, name, value):
        return queryset.filter(Q(costo__status__perfil__nombres__icontains = value) | Q(costo__status__perfil__apellidos__icontains = value))
        return queryset.filter(Q(costo__status__perfil__nombres__icontains = value) | Q(costo__status__perfil__apellidos__icontains = value))

class VacacionesFilter(django_filters.FilterSet):
    nombres = CharFilter(method ='nombres_filter', label="Search")

    class Meta:
        model = Vacaciones
        fields = ['nombres',]

    def nombres_filter(self, queryset, name, value):
        return queryset.filter(Q(status__perfil__nombres__icontains = value) | Q(status__perfil__apellidos__icontains = value))

class UniformesFilter(django_filters.FilterSet):
    nombres = CharFilter(method ='nombres_filter', label="Search")

    class Meta:
        model = Uniformes
        fields = ['nombres',]

    def nombres_filter(self, queryset, name, value):
        return queryset.filter(Q(status__perfil__nombres__icontains = value) | Q(status__perfil__apellidos__icontains = value))

class EconomicosFilter(django_filters.FilterSet):
    nombres = CharFilter(method ='nombres_filter', label="Search")

    class Meta:
        model = Economicos
        fields = ['nombres',]

    def nombres_filter(self, queryset, name, value):
        return queryset.filter(Q(status__perfil__nombres__icontains = value) | Q(status__perfil__apellidos__icontains = value))

class Costo_historicFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name = 'updated_at', lookup_expr='gte')
    end_date = DateFilter(field_name = 'updated_at', lookup_expr='lte')

    class Meta:
        model = Costo
        fields = ['start_date','end_date',]

class CatorcenasFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name = 'fecha_inicial', lookup_expr='gte')
    end_date = DateFilter(field_name = 'fecha_inicial', lookup_expr='lte')

    class Meta:
        model = Catorcenas
        fields = ['start_date','end_date',]

class DistritoFilter(django_filters.FilterSet):
    distrito = django_filters.CharFilter(field_name='distrito', lookup_expr='icontains')
    class Meta:
        model = Distrito
        fields = ['distrito',]

class SolicitudesVacacionesFilter(django_filters.FilterSet):
    numero_de_trabajador = django_filters.NumberFilter(field_name='status__perfil__numero_de_trabajador')
    nombres = CharFilter(method ='nombres_filter', label="Search")
    distrito = django_filters.CharFilter(field_name='status__perfil__distrito__distrito', lookup_expr='icontains')

    class Meta:
        model = Solicitud_vacaciones
        fields = ['nombres','distrito','numero_de_trabajador',]

    def nombres_filter(self, queryset, name, value):
        return queryset.filter(Q(status__perfil__nombres__icontains = value) | Q(status__perfil__apellidos__icontains = value))
    
class SolicitudesEconomicosFilter(django_filters.FilterSet):
    numero_de_trabajador = django_filters.NumberFilter(field_name='status__perfil__numero_de_trabajador')
    nombres = CharFilter(method ='nombres_filter', label="Search")
    distrito = django_filters.CharFilter(field_name='status__perfil__distrito__distrito', lookup_expr='icontains')
    class Meta:
        model = Solicitud_economicos
        fields = ['nombres','distrito','numero_de_trabajador',]
        
    def nombres_filter(self, queryset, name, value):
        return queryset.filter(Q(status__perfil__nombres__icontains = value) | Q(status__perfil__apellidos__icontains = value))
    
