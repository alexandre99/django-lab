from django.shortcuts import render

def index(request):
  return render(request, 'index.html')

def receitas(request):
  return render(request, 'receita.html')
