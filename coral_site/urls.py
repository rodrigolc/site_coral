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
from django.urls import path
from django.conf.urls.static import static
# from rest_framework import routers
from backend import views
from coral_site import settings

# router = routers.DefaultRouter()

# router.register(r'posts', views.PostView, 'post')
# router.register(r'livros', views.LivroView, 'livro')
# router.register(r'textos', views.TextoView, 'texto')
# router.register(r'ilustracoes', views.IlustracaoView,
#                 'ilustracao')
# router.register(r'poemas', views.PoemaView, 'poema')
# router.register(r'colecoes', views.ColecaoView, 'colecao')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    path('', views.index),
    path('ilustra/<int:ilustra_id>/', views.detalhe_ilustra, name='detalhe_ilustra'),
    path('livro/<int:livro_id>/', views.detalhe_livro, name='detalhe_livro'),
    path('poema/<int:poema_id>/', views.detalhe_poema, name='detalhe_poema'),
    path('texto/<int:texto_id>/', views.detalhe_texto, name='detalhe_texto'),
    path('colecao/<int:colecao_id>/', views.detalhe_colecao, name='detalhe_colecao'),
    path('post/<int:post_id>/', views.detalhe_post_redirect, name='detalhe_post_redirect'),
    path('ilustras/', views.ilustras, name='ilustras'),
    path('livros/', views.livros, name='livros'),
    path('poemas/', views.poemas, name='poemas'),
    path('textos/', views.textos, name='textos'),
    path('colecoes/', views.colecoes, name='colecoes'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
