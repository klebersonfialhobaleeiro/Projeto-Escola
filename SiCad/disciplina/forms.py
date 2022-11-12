from django import forms 
from .models import Disciplina
from django.forms import CheckboxSelectMultiple

class DisciplinaForms(forms.ModelForm):
    
    class Meta:
        model = Disciplina
        fields = "__all__"
        widgets = {
            'preRequisito': CheckboxSelectMultiple
        }