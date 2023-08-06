from django.forms import ModelForm # para crear nuestro formulario personalizado
from .models import Task # importa la clase que vas a usar desde models
from django import forms

class TaskForm(forms.ModelForm):

    class Meta:
        model =Task
        fields=['titulo','description','important']
        widgets = { 
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a title' }),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a description' }),

            'important': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }