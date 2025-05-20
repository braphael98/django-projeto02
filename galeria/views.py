from django.shortcuts import render


# Aqui são criadas as views

def index(request): #essa função vai mostar o meu arquivo index, la da pasta templates
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')
