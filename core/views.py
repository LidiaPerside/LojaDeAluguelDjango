from django.shortcuts import render, redirect
from core.models import Itens
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse
from django.contrib.auth.models import User


# Create your views here.

#def index (request):
 #   return redirect('/aluguel/')
def login_users(request):
    return render (request, 'login.html')

def logout_users(request):
    logout(request)
    return redirect('/')

#realiza o login para o usuário ter acesso aos alugueis feitos por ele
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password= request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect( '/')
        else:
            messages.error(request, "Usuário ou senha inválido. Tente novamente")
        return redirect('/')

@login_required(login_url='/login/')
def lista_itens(request):

    usuario = request.user
    #itens = Itens.objects.all()
    data_atual = datetime.now() - timedelta(hour=1)
    #__gt é maior __lt é menor
    itens = Itens.objects.filter(usuario=usuario, data_aluguel__gt=data_atual) #exibe os itens alugados por usuário
    dados = {'itens': itens}
    return render(request, 'aluguel.html', dados)

@login_required(login_url='/login/')
def item (request):
    id_item = request.GET.get('id')
    dados = {}
    if id_item:
        dados['item'] = Itens.objects.get(id=id_item)
    return render (request, 'item.html', dados)

@login_required(login_url='/login/')
def submit_item(request):
    if request.POST:
        item = request.POST.get('item')
        data_aluguel = request.POST.get('data_aluguel')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_item = request.POST.get('id_item')
        if id_item:
            #Itens.objects.filter(id=id_item).update(item=item, data_aluguel=data_aluguel, descricao=descricao)
            item = Itens.objects.get(id=id_item)
            if item.usuario == usuario:
                item.item = item
                item.descricao = descricao
                item.data_aluguel - data_aluguel
                item.save()
        else:
            Itens.objects.create(item=item, data_aluguel=data_aluguel, descricao=descricao, usuario=usuario)

    return redirect('/')

@login_required(login_url='/login/')
def delete_item(request, id_item):
    usuario =request.user
    #Itens.objects.filter(id=id_item).delete()
    try:
        item = Itens.objects.get(id=id_item)
    except Exception:
        raise Http404()
    if usuario == item.usuario:
        item.delete()
    else:
        raise Http404()
    return redirect('/')

#@login_required(login_url='/login/')
def json_lista_item(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)
    #convertendo para o Json conseguir ler
    itens = Itens.objects.filter(usuario=usuario).values('id', 'item')
    #transformando em lista e colocando safe = false por não ser um dicionário
    return JsonResponse(list(itens), safe=False)
