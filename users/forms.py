from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserFieldsMixin:
    def update_user_fields(self, user):
        user.first_name = self.cleaned_data.get('first_name', '')
        user.last_name = self.cleaned_data.get('last_name', '')
        user.email = self.cleaned_data.get('email', '')
        return user

class ProfileForm(UserFieldsMixin, forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=False)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'bio', 'birthdate', 'avatar']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        # Inicializar campos del modelo User
        self.fields['first_name'].initial = user.first_name
        self.fields['last_name'].initial = user.last_name
        self.fields['email'].initial = user.email

    def save(self, commit=True):
        profile = super().save(commit=False)

        # Guardar datos de usuario
        user = profile.user
        self.update_user_fields(user)
        if commit:
            user.save()
            profile.save()
        return profile

class CustomUserCreationForm(UserFieldsMixin, UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False, label='Nombre')
    last_name = forms.CharField(max_length=30, required=False, label='Apellido')

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")
        
    def save(self, commit=True):
        user = super().save(commit=False)
        self.update_user_fields(user)
        if commit:
            user.save()
        return user
