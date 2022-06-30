from ast import Index
from django import views
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.IndexView.as_view(), name='home'),
    path('sobre',views.SobreView.as_view(), name='sobre'),
    path('empresa',views.empresas, name='empresas'),
    path('contato',views.IndexView.as_view(), name='contato'),
    path('empresa/<int:empresa_id>',views.empresas_produtos, name='empresas_produtos'),
]
