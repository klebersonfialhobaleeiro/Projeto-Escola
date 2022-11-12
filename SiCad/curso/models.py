from django.db import models
#from pessoa.models import Professor

# Create your models here.

class Curso(models.Model):
    descricao = models.CharField( max_length=50)
    coordenador = models.ForeignKey(to="pessoa.Professor", related_name="Cordenador", on_delete=models.DO_NOTHING)

    def cadastrar(self):
        return "Aqui cadastrar Curso"

    def __str__(self):#Para aparecer o nome no admin
        return self.descricao
