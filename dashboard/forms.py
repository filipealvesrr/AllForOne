from django import forms
from django.forms import DateInput
# from django.core.exceptions import ValidationError
from dashboard.models import Caso
from authors.forms import add_attr, add_placeholder


class NewCaseForm(forms.ModelForm):
    CATEGORIES = (
        ('Saúde', 'Saúde'),
        ('Educação', 'Educação'),
        ('Alimentação', 'Alimentação'),
        ('Outros', 'Outros'),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['title_of_case'], 'Título do caso')
        add_placeholder(self.fields['description'], 'Descrição')
        add_placeholder(self.fields['value_total'], 'Valor')
        # add_attr(self.fields['title_of_case'], 'class', 'title-case')
        add_attr(self.fields['description'], 'class', 'description')
        add_attr(self.fields['value_total'], 'class', 'value-case')
        add_attr(self.fields['date_expiration'], 'class', 'date-end')

    date_expiration = forms.DateField(
        required=True,
        widget=DateInput(attrs={'type': 'date'})
    )

    category = forms.ChoiceField(
        choices=CATEGORIES,
        widget=forms.Select(attrs={'class': 'selection'})
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
