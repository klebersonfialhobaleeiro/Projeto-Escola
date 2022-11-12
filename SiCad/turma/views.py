from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
from pessoa.models import Aluno
from .models import Turma

# Create your views here.

def home(request):
    return render(request, 'turma/home.html')

def listar_turmas(request):
    if request.method == "GET":
        turmas = Turma.objects.all()
        context = {
            'turmas':turmas,
        }
        return render(request, 'turma/listaTurma.html', context)

def excluir_turma(request, turma_id):
    Turma.objects.get(pk=turma_id).delete()
    return redirect(reverse('listar_turmas'))

def matricular_turma(request):
    if request.method == "GET":
        return render(request, 'turma/turmas.html')   
    
    if request.method == "POST":
        ano = request.POST.get('ano')
        semestre = request.POST.get('semestre')
        diaSemana = request.POST.get('diaSemana')
        horarios = request.POST.get('horarios')

        Turma.objects.create(ano=ano,
                                semestre=semestre,
                                diaSemana=diaSemana,
                                horarios=horarios,)

        messages.add_message(request, messages.SUCCESS, 'Turma cadastrado')
        return redirect(reverse('matricular_turma'))

def matricular_aluno_turma(request):
    if request.method == "GET":
        aluno = Aluno.objects.all()
        turmas = Turma.objects.all()
        context = {
            'aluno':aluno,
            'turmas':turmas,
        }
        return render(request, 'turma/aluno_turma.html', context)
    
    if request.method == 'POST':
        turma = Turma.objects.get(pk = int(request.POST.get('turma')))
        alunos = request.POST.getlist('aluno')

        for aluno in alunos:
            aluno = Aluno.objects.get(pk=int(aluno))
            turma.matricularAluno(aluno)

        messages.add_message(request, messages.SUCCESS, 'Aluno cadastrado na turma')
        return redirect(reverse('matricular_aluno_turma'))