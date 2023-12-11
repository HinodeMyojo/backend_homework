from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from .models import Contest, Congratulation

OBSCENE_WORDS = {'Хуй', 'Пизда'}

class ContestForm(forms.ModelForm):

    class Meta:
        model = Contest
        exclude = ('author', )
        widgets = {
            'description': forms.Textarea({'cols': '22', 'rows': '5'}),
            'comment': forms.Textarea({'cols': '22', 'rows': '5'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        return title.split()[0]
    
    def clean(self) -> dict[str, Any]:
        super().clean()
        title = self.cleaned_data['title']
        if title in OBSCENE_WORDS:
            send_mail(
                subject='Тестовый отправитель',
                message='Тестовый получатель',
                from_email='hideem@mail.ru',
                recipient_list=['hinodem@mail.ru'],
                fail_silently=True
            )
            raise ValidationError(
                'Да иди ты нахуй'
            )

class CongratulationForm(forms.ModelForm):
    class Meta:
        model = Congratulation
        fields = ('text',)