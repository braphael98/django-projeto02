from django.db import models

#Aqui esta nossas classes, para usarmos no banco de dados

class Fotografia(models.Model):
    nome = models.CharField(max_length= 100, null= False, blank= False) #atribuindo o atributo nome, sendo uma string de até 100 caracteres
    legenda = models.CharField(max_length= 150, null= False, blank= False)
    descricao = models.TextField(null= False, blank= False)
    foto = models.CharField(max_length= 100, null= False, blank= False)

    def __str__(self): #função afim de retornar o nome da fotografia, para saber se esta ok 
        return f"Fotografia [nome{self.nome}]"
    
    #feito isso basta rodar python manage.py makemigrations para criar as tabelas 
