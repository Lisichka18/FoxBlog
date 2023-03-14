from django.forms import ModelForm, TextInput, Textarea
from .models import Articles


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ["name", "content"]
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })
        }