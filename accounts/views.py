from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomSignupForm, CustomLoginForm, CustomProfileForm
from allauth.account.views import SignupView, LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def profile_view(request):
    # Requiere que el usuario esté autenticado para acceder a esta vista

    user = request.user

    if request.method == 'POST':
        # Si la solicitud es una POST (es decir, se envió un formulario)
        
        form = CustomProfileForm(request.POST)
        # Crea una instancia del formulario con los datos enviados en la solicitud POST
        
        if form.is_valid():
            # Si el formulario es válido (todos los campos pasan las validaciones)

            # Actualizar los datos del perfil del usuario
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password'])
            user.username = form.cleaned_data['username']
            user.save()

            return redirect('accounts:profile')
            # Redirige al usuario a la página de perfil (cambia 'profile' por la URL deseada)
            
    else:
        # Si la solicitud no es una POST (es decir, es una GET)

        form = CustomProfileForm(initial={
            'email': user.email,
            'username': user.username,
        })
        # Crea una instancia del formulario con los datos iniciales del usuario

    context = {
        'form': form,
    }
    # Crea un diccionario de contexto con el formulario

    return render(request, 'accounts/profile.html', context)
    # Renderiza la plantilla 'accounts/profile.html' con el diccionario de contexto y devuelve la respuesta HTML al cliente

def logout_view(request):
    logout(request)
    return redirect('home')


class CustomSignupView(SignupView):
    form_class = CustomSignupForm
    template_name = 'accounts/signup.html'
    success_url = '/accounts/profile/'

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'accounts/login.html'
    success_url = '/'  # Cambia '/' por la URL deseada después del inicio de sesión


def signup_view(request):
    # Redirige a la vista de registro personalizada
    return CustomSignupView.as_view()(request)

def login_view(request):
    # Redirige a la vista de inicio de sesión personalizada
    return CustomLoginView.as_view()(request)
