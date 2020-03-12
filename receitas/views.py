from django.shortcuts import render

def index(request):
  receitas = {
    1: 'Lasanha',
    2: 'Sopa de legumes',
    3: 'Sorvete'
  }
  dados = {
    'nomes_das_receitas': receitas
  }
  return render(request, 'index.html', dados)

def receitas(request):
  return render(request, 'receita.html')
