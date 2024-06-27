from django.urls import path
from . import views

urlpatterns = [
    path('produccion-total/', views.total_produccion_api, name='total_produccion_api'),
    path('produccion-filtrada/', views.produccion_filtrada_api, name='produccion_filtrada_api'),
    # Otras rutas para API según los requisitos de la autoridad fiscalizadora
]
