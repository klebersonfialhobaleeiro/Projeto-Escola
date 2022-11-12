from django.db import models

# Create your models here.

class Disciplina(models.Model):
    descricao = models.CharField(max_length=50)
    cargaHoraria = models.IntegerField()
    ementa = models.CharField(max_length=2000)
    bibliografia = models.CharField(max_length=2000)
    preRequisito = models.ManyToManyField("self", verbose_name=("preRequisito"), null=True, blank=True)
    
    def cadastrar(self):
        return "Aqui vai cadastrar a Disciplina" 

    def __str__(self):#Para aparecer o nome no admin
        return self.descricao