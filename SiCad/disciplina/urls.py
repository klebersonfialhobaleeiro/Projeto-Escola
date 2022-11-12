from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_disciplina/', views.cadastrar_disciplina, name="cadastrar_disciplina"),
]