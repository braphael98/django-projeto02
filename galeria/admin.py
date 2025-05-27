from django.contrib import admin
from galeria.models import Fotografia #todo objeto que queremos acessar pela aba de admin tem que ser importada para ca


class ListandoFotos(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda","publicada")#lista os itens do banco de dados
    list_display_links = ("id", "nome") #podemos acessar os dados do banco com clicks intuivos
    search_fields = ("nome",) #aqui é para buscar os itens com o nome
    list_filter = ("categoria",) #faz um filtro de listas em admin
    list_editable = ("publicada",)
    list_per_page = 10; #numero de itens por pagina, no caso 10 

admin.site.register(Fotografia, ListandoFotos) #registar a classe no django admin
