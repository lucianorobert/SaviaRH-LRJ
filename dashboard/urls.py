from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Mensaje', views.mensaje, name='Mensaje.html'),
    path('dashboard/render_report/<int:pk>/',views.render_report, name='render_report'),
]