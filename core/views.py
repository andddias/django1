from django.shortcuts import render


def index(request):
    # Usando informações do Django Shell
    print(dir(request.user))
    print(f"User: {request.user}")

    # Logica para saber se usuario está logado
    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário não logado'
    else:
        teste = 'Usuário logado'

    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa!',
        'logado': teste,
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
