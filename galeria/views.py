from django.shortcuts import render



# Aqui são criadas as views
#essa função vai mostar o meu arquivo index, la da pasta templates
def index(request):
    dados ={ #dicionario para ter dados nos nossos cards
    1:{"nome": "Nebulosa",
       "legenda": "webbtelescope.org / NASA /James Webb"},
    2:{"nome": "Galaxia NGC 1079",
       "legenda": "nasa.org/ NASA / Hubble"}
}
    return render(request, 'galeria/index.html',{"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')
