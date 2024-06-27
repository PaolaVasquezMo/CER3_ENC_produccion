from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página principal de producción (ejemplo)
    path('registro/', views.registro_produccion, name='registro_produccion'),
    path('modificacion/<int:id>/', views.modificar_produccion, name='modificar_produccion'),
    path('consulta/', views.consulta_produccion, name='consulta_produccion'),
    # Otras rutas según los requisitos funcionales
]