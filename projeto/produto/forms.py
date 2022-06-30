from .models import Produto, Produto_Empresa
from django.forms import ModelForm


class ProdutoForm(ModelForm):
    
    class Meta:
        model = Produto
        fields = "__all__"

class Produto_EmpresaForm(ModelForm):
    
    class Meta:
        model = Produto_Empresa
        fields = "__all__"