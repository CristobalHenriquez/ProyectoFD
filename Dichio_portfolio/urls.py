
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from accounts import views as account_views
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,  name='home'),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
