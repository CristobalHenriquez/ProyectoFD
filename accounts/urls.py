from django.contrib import admin
from django.urls import path
from accounts import views as account_views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', account_views.login_view, name='login'),
    path('signup/', account_views.signup_view, name='signup'),
    path('profile/', account_views.profile_view, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
    # Otras rutas de la aplicación
]
