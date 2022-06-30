from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:empresa_id>/', views.detail, name='detail'),
    path('excluir/<int:empresa_id>/', views.excluir, name='excluir'),
    path('criar/', views.criar, name='criar'),
    path('editar/<int:empresa_id>/', views.editar, name='editar'),
    path('teste', views.upload, name='upload'),
    path('template/', views.template, name="template")
]