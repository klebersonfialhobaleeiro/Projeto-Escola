from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    #dados do aluno
    path('listar_alunos/', views.listar_alunos, name="listar_alunos"),
    path('excluir_aluno/<int:aluno_id>/', views.excluir_aluno, name="excluir_aluno"),
    path('matricular_aluno/', views.matricular_aluno, name="matricular_aluno"),
]