from django.shortcuts import redirect, render
from .models import Disciplina
from .forms import DisciplinaForms

# Create your views here.

def cadastrar_disciplina(request):
    if request.method == "GET":
        formDisciplina = DisciplinaForms
        context={
                'formDisciplina':formDisciplina,
        }
        return render(request, 'disciplina/disciplina.html', context)   

    if request.method == 'POST':
        formDisciplina = DisciplinaForms(request.POST)
        if formDisciplina.is_valid():
            Disciplina = formDisciplina.save()
            return redirect('/')