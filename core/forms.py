from django import forms
from core.models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model =Todo
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
           }