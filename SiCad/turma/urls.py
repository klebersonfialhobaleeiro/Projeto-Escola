from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('listar_turmas/', views.listar_turmas, name="listar_turmas"),
    path('excluir_turma/<int:turma_id>/', views.excluir_turma, name="excluir_turma"),
    path('matricular_turma/', views.matricular_turma, name="matricular_turma"),
    path('matricular_aluno_turma/', views.matricular_aluno_turma, name="matricular_aluno_turma"),
]