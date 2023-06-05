from django.shortcuts import redirect
from django.urls import reverse

class AdminRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Se ejecuta cada vez que se recibe una solicitud HTTP

        # Llama a la función de respuesta original
        response = self.get_response(request)

        # Verifica si la solicitud es para la página de inicio de sesión del administrador ("/admin/login/")
        # y si el usuario está autenticado
        if request.path == '/admin/login/' and request.user.is_authenticated:
            # Redirige al índice del administrador ("/admin/")
            return redirect(reverse('/admin/'))

        # Devuelve la respuesta original
        return response
