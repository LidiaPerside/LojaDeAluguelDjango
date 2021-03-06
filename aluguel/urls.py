"""aluguel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aluguel/', views.lista_itens),
   path('aluguel/lista/<int:id_usuario>/', views.json_lista_item),
    path('aluguel/lista/', views.item),
    path('aluguel/item/submit', views.submit_item),
    path('aluguel/item/delete/<int:id_item>/', views.delete_item),
    #path('', views.index),
    path ('', RedirectView.as_view(url='/aluguel/')),
    path('login/', views.login_users),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_users)
]
