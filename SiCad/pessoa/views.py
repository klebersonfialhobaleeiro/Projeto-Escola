from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from turma.models import Turma
from pessoa.models import Aluno
# Create your views here.

def home(request):
    return render(request, 'pessoa/home.html')

def listar_alunos(request):
    if request.method == "GET":
        alunos = Aluno.objects.all()
        context ={
            'alunos':alunos,
        }
        return render(request, 'pessoa/listaAlunos.html', context)

def excluir_aluno(request, aluno_id):
    Aluno.objects.get(pk=aluno_id).delete()
    return redirect(reverse('listar_alunos'))

def matricular_aluno(request):
    redirect_to = redirect(reverse('matricular_aluno'))

    if request.META.get("QUERY_STRING"):
        query_string = request.META.get("QUERY_STRING").split("=")[1]
        redirect_to = redirect(reverse('matricular_aluno')) if query_string == "0" else redirect(reverse('matricular_aluno_turma'))
    if request.method == "GET":
        return render(request, 'pessoa/alunos.html')   
    
    if request.method == "POST":
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        matricula = request.POST.get('matricula')
        situacao = request.POST.get('situacao')

        aluno = Aluno.objects.filter(matricula=matricula)

        if aluno.exists():
            messages.add_message(request, messages.ERROR, 'Matricula já existe')
            return redirect_to

        aluno = Aluno.objects.create(nome=nome,
                                            endereco=endereco,
                                            telefone=telefone,
                                            matricula=matricula,
                                            situacao=situacao,)

        messages.add_message(request, messages.SUCCESS, 'Aluno cadastrado')
        return redirect_to