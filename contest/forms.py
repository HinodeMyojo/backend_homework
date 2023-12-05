from django import forms

from .models import Contest


class ContestForm(forms.ModelForm):

    class Meta:
        model = Contest
        fields = '__all__'
        widgets = {
            'description': forms.Textarea({'cols': '22', 'rows': '5'}),
            'comment': forms.Textarea({'cols': '22', 'rows': '5'}),
        }