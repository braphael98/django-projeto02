from django.db import models
from datetime import datetime
#Aqui esta nossas classes, para usarmos no banco de dados

class Fotografia(models.Model):
    #lista de tupulas que define as opções para um campo de categoria.
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALAXIA","Galaxia"),
        ("PLANETA","Planeta"),
    ]

    nome = models.CharField(max_length= 100, null= False, blank= False) #atribuindo o atributo nome, sendo uma string de até 100 caracteres
    legenda = models.CharField(max_length= 150, null= False, blank= False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null= False, blank= False)
    foto = models.CharField(max_length= 100, null= False, blank= False) 
    publicada = models.BooleanField(default=False) #atributo de checkbox boolean para a publicação
    data_fotografia = models.DateTimeField(default = datetime.now, blank= False)# adicionando uma data com a importação do datetime

    def __str__(self): #função afim de retornar o nome da fotografia, para saber se esta ok 
        return f"Fotografia [nome{self.nome}]"
    
    #feito isso basta rodar python manage.py makemigrations para criar as tabelas 
