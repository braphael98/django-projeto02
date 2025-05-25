from django.contrib import admin
from galeria.models import Fotografia #todo objeto que queremos acessar pela aba de admin tem que ser importada para ca


class ListandoFotos(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda")#lista os itens do banco de dados
    list_display_links = ("id", "nome") #podemos acessar os dados do banco com clicks intuivos
    search_fields = ("nome",) #aqui é para buscar os itens com o nome
    list_filter = ("categoria",)
admin.site.register(Fotografia, ListandoFotos) #registar a classe no django admin
