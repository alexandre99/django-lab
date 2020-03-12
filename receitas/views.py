from django.shortcuts import render
from .models import Receita

def index(request):
    receitas_bd = Receita.objects.all()

    dados = {
        'receitas': receitas_bd
    }
    return render(request, 'index.html', dados)

def receitas(request):
    return render(request, 'receita.html')
