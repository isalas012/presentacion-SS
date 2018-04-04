from django.forms import ModelForm, Textarea, TextInput
from .models import article, comment

class articleForm(ModelForm):
    class Meta:
        model = article
        fields = ('title', 'content', 'author')
        widgets = {
            'title': TextInput(attrs={'class' : 'form-control'}),
            'content': Textarea(attrs={'cols': 80, 'rows': 20, 'class' : 'form-control'}),
            'author': TextInput(attrs={'class' : 'form-control'})
        }
        labels = {
            'title': 'Título',
            'content': 'Contenido',
            'autor': 'Autor'
        }

class commentForm(ModelForm):
    class Meta:
        model = comment
        fields = ('content', 'author')
        widgets = {
            'content': TextInput(attrs={'class' : 'form-control'}),
            'author': TextInput(attrs={'class' : 'form-control'})
        }
        labels = {
            'content': 'Contenido',
            'author': 'Autor'
        }
