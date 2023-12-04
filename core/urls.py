from django.urls import path
from . import views


urlpatterns = [
     path('talleres/', views.lista_talleres, name='lista_talleres'),
     path('info/<int:taller_id>/', views.detalle_taller, name='informacion_talleres'),
     path('programar-cita/', views.programar_cita, name='programar_cita'),
]