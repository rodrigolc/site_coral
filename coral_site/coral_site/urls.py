"""coral_site URL Configuration

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
from django.urls import path, include
from rest_framework import routers                    # add this
from backend import views

router = routers.DefaultRouter()                      # add this

router.register(r'posts', views.PostView, 'post')     # add this
router.register(r'livros', views.LivroView, 'livro')     # add this
router.register(r'textos', views.TextoView, 'texto')     # add this
router.register(r'ilustracoes', views.IlustracaoView, 'ilustracao')     # add this
router.register(r'poemas', views.PoemaView, 'poema')     # add this
router.register(r'colecoes', views.ColecaoView, 'colecao')     # add this

urlpatterns = [
    path('admin/', admin.site.urls),         path('api/', include(router.urls))                # add this
]

