from django import forms
from django.forms import DateInput
from dashboard.models import Caso, Category, Donate
from authors.forms import add_attr, add_placeholder


class NewCaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['title_of_case'], 'Título do caso')
        add_placeholder(self.fields['description'], 'Descrição')
        add_placeholder(self.fields['value_total'], 'Valor')
        add_attr(self.fields['description'], 'class', 'description')
        add_attr(self.fields['value_total'], 'class', 'value-case')
        add_attr(self.fields['date_expiration'], 'class', 'date-end')

    date_expiration = forms.DateField(
        required=True,
        widget=DateInput(attrs={'type': 'date'}),
        error_messages={
            'required': 'Esse campo não pode ser vazio'
        },
    )

    category = forms.ModelChoiceField(
        required=True,
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'selection'}),
        error_messages={
            'required': 'Esse campo não pode ser vazio'
        },
    )

    class Meta:
        model = Caso
        fields = [
            'title_of_case',
            'category',
            'description',
            'value_total',
            'date_expiration'
        ]

        widgets = {
            'value_total': forms.NumberInput(attrs={'min': 0, 'pattern': '^[0-9]*\.?[0-9]+$'})  # noqa E501
        }


class DonateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['value_of_donate'], 'Valor da doação')
        add_attr(self.fields['value_of_donate'], 'class', 'field_large')

    class Meta:
        model = Donate
        fields = [
            'value_of_donate',
        ]

        widgets = {
            'value_of_donate': forms.NumberInput(attrs={'min': 0, 'pattern': '^[0-9]*\.?[0-9]+$'})  # noqa E501
        }
