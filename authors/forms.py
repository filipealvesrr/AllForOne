from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# from dashboard.models import Caso
import re


def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'A senha deve ter pelo menos uma letra maiúscula, '
            'uma letra minúscula e um número. '
            'O comprimento deve ser de pelo menos 8 caracteres.'
        ),
            code='invalid'
        )


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['first_name'], 'Nome')
        add_placeholder(self.fields['last_name'], 'Sobrenome')
        add_placeholder(self.fields['username'], 'Username')
        add_placeholder(self.fields['email'], 'Email')
        add_placeholder(self.fields['password'], 'Senha')
        add_attr(self.fields['first_name'], 'class', 'field_large')
        add_attr(self.fields['last_name'], 'class', 'field_large')
        add_attr(self.fields['username'], 'class', 'field_large')
        add_attr(self.fields['email'], 'class', 'field_large')
        add_attr(self.fields['password'], 'class', 'field_large')

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': ''
        }),
        error_messages={
            'required': 'Esse campo não pode ser vazio'
        },
        validators=[strong_password]
    )

    first_name = forms.CharField(
        required=True,
        error_messages={
            'required': 'Esse campo não pode ser vazio'
        },
    )

    last_name = forms.CharField(
        required=True,
        error_messages={
            'required': 'Esse campo não pode ser vazio'
        },
    )
    username = forms.CharField(
        required=True,
        error_messages={
            'required': 'Esse campo não pode ser vazio'
        },
    )
    email = forms.CharField(
        required=True,
        error_messages={
            'required': 'Esse campo não pode ser vazio'
        },
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'Esse e-mail já foi cadastrado na plataforma!',
                code='invalid',)

        return email


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Username')
        add_placeholder(self.fields['password'], 'Senha')
        add_attr(self.fields['username'], 'class', 'fields')
        add_attr(self.fields['password'], 'class', 'fields')

    username = forms.CharField(

    )
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
