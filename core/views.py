from django.shortcuts import render

from .models import Produto


def index(request):
    # Usando informações do Django Shell
    print(dir(request.user))
    print(f"User: {request.user}")

    # Logica para saber se usuario está logado
    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário não logado'
    else:
        teste = 'Usuário logado'

    # Obtendo produtos cadastrados no bando de dados
    produtos = Produto.objects.all()

    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa!',
        'logado': teste,
        'produtos': produtos,
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    prod = Produto.objects.get(id=pk)

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)
