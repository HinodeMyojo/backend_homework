from typing import Any
from django import forms
from django.core.exceptions import ValidationError

from .models import Contest

OBSCENE_WORDS = {'Хуй', 'Пизда'}

class ContestForm(forms.ModelForm):

    class Meta:
        model = Contest
        fields = '__all__'
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
            raise ValidationError('Да иди ты нахуй!')
