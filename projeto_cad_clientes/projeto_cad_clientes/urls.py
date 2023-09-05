from django.urls import path
from app_cad_clientes import views

urlpatterns = [
    # rota, view responsável, nome de referência
    path('',views.home,name='home'),
]
