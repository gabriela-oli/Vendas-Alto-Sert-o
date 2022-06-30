from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from produto.forms import ProdutoForm,Produto_EmpresaForm
from .models import Produto, Produto_Empresa
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    produto = Produto.objects.all()
    context = {
        'produtos': produto,
    }
    return render(request, 'produto/listar.html', context)

@login_required
def detail(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    
    context = {
        'produto' : produto
    }
    
    return render(request, 'produto/detail.html', context)

@login_required
def excluir(request, produto_id):
    
    Produto.objects.get(pk=produto_id).delete()
    
    return HttpResponseRedirect("/produto")

@login_required
def criar(request):
    
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/produto")
    else:
        form = ProdutoForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'produto/formCriar.html', context)

@login_required
def editar(request, produto_id):
    
    produto = Produto.objects.get(id=produto_id)
    
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/produto")
    else:
        form = ProdutoForm(instance=produto)
    
    context = {
        'form': form,
        'produto_id': produto_id
    }
    
    
    return render(request, 'produto/editForm.html', context)

def base(request):
    return render(request,'base.html')


# ---Produto_Empresa-------------
@login_required
def index_produto_empresa(request):
    produto = Produto_Empresa.objects.all()
    context = {
        'produtos': produto,
    }
    return render(request, 'produto_empresa/listar.html', context)

@login_required
def detail_produto_empresa(request, produto_empresa_id):
    produto = Produto_Empresa.objects.get(pk=produto_empresa_id)
    
    context = {
        'produto' : produto
    }
    
    return render(request, 'produto_empresa/detail.html', context)

@login_required
def excluir_produto_empresa(request, produto_empresa_id):
    
    Produto_Empresa.objects.get(pk=produto_empresa_id).delete()
    
    return HttpResponseRedirect("/produto/produto_empresa")

@login_required
def criar_produto_empresa(request):
    
    if request.method == "POST":
        form = Produto_EmpresaForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/produto/produto_empresa")
    else:
        form = Produto_EmpresaForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'produto_empresa/formCriar.html', context)

@login_required
def editar_produto_empresa(request, produto_empresa_id):
    
    produto = Produto_Empresa.objects.get(pk=produto_empresa_id)
    
    if request.method == "POST":
        form = Produto_EmpresaForm(request.POST, instance=produto)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/produto")
    else:
        form = Produto_EmpresaForm(instance=produto)
    
    context = {
        'form': form,
        'produto_empresa_id': produto_empresa_id
    }
    
    
    return render(request, 'produto_empresa/editForm.html', context)

def base(request):
    return render(request,'base.html')