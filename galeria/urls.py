from django.urls import path
from galeria.views import index, imagem

urlpatterns = [ #foi passado o id pela URL (não sei se isso é uma boa pratica mas ok, segui os passos do cursinho)
     path('',index, name = 'index'),
     path('imagem/<int:foto_id>', imagem, name ='imagem'), 
]