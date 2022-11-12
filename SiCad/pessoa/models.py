from django.db import models
from turma.models import Turma
#from curso.models import Curso

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    
    def cadastrar(self):
        return "Aqui vai cadastrar Pessoa"

class Professor(Pessoa):
    titulacaoMaxima = models.CharField(max_length=100)
    alocado = models.ManyToManyField(to='curso.Curso', verbose_name=("Alocado"))

    def cadastrar(self):
        return "Aqui vai cadastrar Professor"


class Aluno(Pessoa):
    matricula = models.CharField(max_length=50)
    situacao = models.CharField(max_length=50)
    turma =  models.ManyToManyField(to="turma.Turma", related_name='Aluno_Turma', blank=True)

    def __str__(self):#Para aparecer o nome no admin
        return self.nome

    def matricularCurso(self):
        return "Aqui vai matricular Aluno"

    def trancar(self):
        return "Aqui vai trancar a matricula do Aluno"

    def formar(self):
        return "Aqui vai formar o Aluno"

    def evadir(self):
        return "Aqui vai evadir o Aluno"

    def obterAvaliacoes(self):
        return "Aqui vai obter avaliações do Aluno"

    def emitirHistorico(self):
        return "Aqui vai emitir o histórico do Aluno"

