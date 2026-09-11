from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro_medico/', views.register_medico, name='register_medico'),
    path('cadastro_paciente/', views.register_paciente, name='register_paciente'),
    path('marcar_consulta/', views.register_consulta, name='register_consulta'),
]
