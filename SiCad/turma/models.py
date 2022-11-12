from django.db import models

# Create your models here.

class Turma(models.Model):
    ano = models.IntegerField()
    semestre = models.IntegerField()
    diaSemana = models.IntegerField()
    horarios = models.CharField(max_length=100)

    def abrirTurma(self):
        return "Aqui vai abrir turma"

    def alocarProfessor(self):
        return "Aqui vai alocar professor"

    def matricularAluno(self, aluno):
        aluno.turma.add(self)
        return 

    def emitirDiario(self):
        return "Aqui vai emitir diário"

class Avaliacao(models.Model):
    turma = models.ForeignKey(to='turma.Turma', on_delete=models.DO_NOTHING)
    alunos = models.ForeignKey(to='pessoa.Aluno',on_delete=models.DO_NOTHING)

    nota1 = models.FloatField()
    nota2 = models.FloatField()
    notaProvaFinal = models.FloatField()
    frequencia = models.IntegerField()

    def lancarAvaliacao(self):
        return "Aqui vai lançar avaliação "

    def calcularAprovacao(self):
        return "Aqui vai calcular a aprovação"
