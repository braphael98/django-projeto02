from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia #Aqui importa as classes !

def index(request):
    fotografias = Fotografia.objects.filter(publicada = True) #agora ele mostra apenas as fotos que estao marcadas como publicadas no admin do banco de dados
    return render(request, 'galeria/index.html',{"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html',{"fotografia": fotografia})
