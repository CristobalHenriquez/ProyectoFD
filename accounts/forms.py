from .models import Profile
from django import forms
from allauth.account.forms import SignupForm, LoginForm

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personaliza los campos del formulario de registro
        self.fields['username'].widget.attrs.update({'placeholder': 'Nombre de usuario'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Correo electrónico'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Contraseña'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirmar contraseña'})

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personaliza los campos del formulario de inicio de sesión
        self.fields['login'].widget.attrs.update({'placeholder': 'Nombre de usuario o correo electrónico'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Contraseña'})

class CustomProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'password', 'username']

    # Personaliza las etiquetas de los campos si es necesario
    email = forms.EmailField(label='Correo electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    username = forms.CharField(label='Nombre de usuario', max_length=100)