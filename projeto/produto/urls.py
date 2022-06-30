from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:produto_id>/', views.detail, name='detail'),
    path('excluir/<int:produto_id>/', views.excluir, name='excluir'),
    path('criar/', views.criar, name='criar'),
    path('editar/<int:produto_id>/', views.editar, name='editar'),
    path('produto_empresa', views.index_produto_empresa, name='index_produto_empresa'),
    path('produto_empresa/<int:produto_empresa_id>/', views.detail_produto_empresa, name='detail_produto_empresa'),
    path('produto_empresa/excluir/<int:produto_empresa_id>/', views.excluir_produto_empresa, name='excluir_produto_empresa'),
    path('produto_empresa/criar', views.criar_produto_empresa, name='criar_produto_empresa'),
    path('produto_empresa/editar/<produto_empresa_id>/', views.editar_produto_empresa, name='editar_produto_empresa'),
]

