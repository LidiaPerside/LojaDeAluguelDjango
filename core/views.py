from django.shortcuts import render, redirect
from core.models import Itens

# Create your views here.

#def index (request):
 #   return redirect('/aluguel/')


def lista_itens(request):

    usuario = request.user
    itens = Itens.objects.all()

    #itens = Itens.objects.filter(usuario=usuario) #exibe os itens alugados por usuário
    dados = {'itens': itens}
    return render(request, 'aluguel.html', dados)