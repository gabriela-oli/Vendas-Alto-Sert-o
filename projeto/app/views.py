from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import (get_object_or_404,render,HttpResponseRedirect)
from empresa.models import Empresa
from produto.models import Produto,Produto_Empresa

class IndexView(TemplateView):
    template_name = 'index.html'


class SobreView(TemplateView):
    template_name = 'about.html'
    
class LocaisView(TemplateView):
    template_name = 'portfolio.html'
    
class ProdutosView(TemplateView):
    template_name = 'service.html'

def empresas(request):
    empresa = Empresa.objects.all()
    context = {
        'empresas': empresa,
    }
    return render(request, 'service.html', context)

# def empresas_produtos(request):
#     empresas_produtos = Produto_Empresa.objects.all()
#     context = {
#         'produto': empresas_produtos,
#     }
#     return render(request, 'produto-empresa.html', context)



def empresas_produtos(request, empresa_id):
    empresa = Empresa.objects.get(pk=empresa_id)
    produto = Produto_Empresa.objects.all()
    context = {
        'empresa' : empresa,
        'produto' : produto
    }
    return render(request, 'produto-empresa.html', context)
    