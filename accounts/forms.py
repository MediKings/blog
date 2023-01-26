from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Prénom"}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}),
        }
