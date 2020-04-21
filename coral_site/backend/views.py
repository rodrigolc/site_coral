from django.shortcuts import render
from rest_framework import viewsets          # add this
# add this
from .serializers import PostSerializer, LivroSerializer, TextoSerializer, IlustracaoSerializer, PoemaSerializer, ColecaoSerializer
# add this
from .models import Post, Livro, Texto, Ilustracao, Poema, Colecao

# Create your views here.


class PostView(viewsets.ModelViewSet):       # add this
    serializer_class = PostSerializer          # add this
    queryset = Post.objects.all()              # add this


class LivroView(viewsets.ModelViewSet):       # add this
    serializer_class = LivroSerializer          # add this
    queryset = Livro.objects.all()              # add this


class TextoView(viewsets.ModelViewSet):       # add this
    serializer_class = TextoSerializer          # add this
    queryset = Texto.objects.all()              # add this


class IlustracaoView(viewsets.ModelViewSet):       # add this
    serializer_class = IlustracaoSerializer          # add this
    queryset = Ilustracao.objects.all()              # add this


class PoemaView(viewsets.ModelViewSet):       # add this
    serializer_class = PoemaSerializer          # add this
    queryset = Poema.objects.all()              # add this


class ColecaoView(viewsets.ModelViewSet):       # add this
    serializer_class = ColecaoSerializer          # add this
    queryset = Colecao.objects.all()              # add this
