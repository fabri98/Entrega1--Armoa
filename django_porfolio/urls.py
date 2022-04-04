"""django_porfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from portfolio import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('comentario/', views.cargar_comentario, name='comentario'),
    path('usuarios/', views.projecto_usuario, name='projecto_usuario'),
    path('login/', views.login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name='home.html'), name="logout"),
    path('register/', views.register, name="register"),
    path('edit/', views.edit, name="edit")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
