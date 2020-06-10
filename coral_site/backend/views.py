
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer, LivroSerializer, TextoSerializer, IlustracaoSerializer, PoemaSerializer, ColecaoSerializer, TagSerializer
from .models import Post, Livro, Texto, Ilustracao, Poema, Colecao, Tag
from django.http import Http404
from django.shortcuts import get_object_or_404, render
# Create your views here.

class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class LivroView(viewsets.ModelViewSet):
    serializer_class = LivroSerializer
    queryset = Livro.objects.all()

class TextoView(viewsets.ModelViewSet):
    serializer_class = TextoSerializer
    queryset = Texto.objects.all()

class IlustracaoView(viewsets.ModelViewSet):
    serializer_class = IlustracaoSerializer
    queryset = Ilustracao.objects.all()

class PoemaView(viewsets.ModelViewSet):
    serializer_class = PoemaSerializer
    queryset = Poema.objects.all()

class ColecaoView(viewsets.ModelViewSet):
    serializer_class = ColecaoSerializer
    queryset = Colecao.objects.all()

class TagView(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

def view_ilustra(request, ilustra_id):
    try:
        ilustra = Ilustracao.objects.get(pk=ilustra_id)
    except Ilustracao.DoesNotExist:
        raise Http404("Ilustração não encontrada")
    return render(request, 'ilustra.html', {'ilustra': ilustra})

def view_texto(request, texto_id):
    try:
        texto = Texto.objects.get(pk=texto_id)
    except Texto.DoesNotExist:
        raise Http404("Texto não encontrado.")
    return render(request, 'texto.html', {'texto': texto})

def view_livro(request, livro_id):
    try:
        livro = Livro.objects.get(pk=livro_id)
    except Livro.DoesNotExist:
        raise Http404("livro não encontrado")
    return render(request, 'livro.html', {'livro': livro})

def view_poema(request, poema_id):
    try:
        poema = Poema.objects.get(pk=poema_id)
    except Poema.DoesNotExist:
        raise Http404("Poema não encontrado")
    return render(request, 'poema.html', {'poema': poema})

#Post, Livro, Texto, Ilustracao, Poema, Colecao, Tag

def index(request):
    latest_posts = Post.objects.order_by('-data_publicacao')[:10].select_subclasses()
    context = {'latest_posts': latest_posts}
    return render(request, 'backend/index.html', context)

def detalhe_ilustra(request, ilustra_id):
    ilustra = get_object_or_404(Ilustracao, id=ilustra_id)
    context = {'ilustra': ilustra}
    return render(request, 'backend/ilustra.html', context)

def detalhe_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    context = {'livro': livro}
    return render(request, 'backend/livro.html', context)

def detalhe_poema(request, poema_id):
    poema = get_object_or_404(Poema, id=poema_id)
    context = {'poema': poema}
    return render(request, 'backend/poema.html', context)

def detalhe_texto(request, texto_id):
    texto = get_object_or_404(Texto, id=texto_id)
    context = {'texto': texto}
    return render(request, 'backend/texto.html', context)
    