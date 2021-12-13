from .models import Refences, Text
from django.forms import ModelForm, TextInput, Textarea, Form, CharField


class ReferencesForm(Form):
    title = CharField(
        label='Загаловок',max_length=300, widget= TextInput(attrs={'placeholder': 'Введите заголовок ',
                               'class': 'form-control'}))
    text = CharField(
        label='Текст ', max_length=10000,
        widget=Textarea(attrs={'placeholder': 'Введите текст ',
                               'class': 'form-control'}))


